#!/usr/bin/env python3
"""Verify and restore the public Market Heat handoff without replacing existing work."""
import argparse,hashlib,json,pathlib,tarfile,tempfile,shutil,os,subprocess
p=argparse.ArgumentParser();p.add_argument('--output',default='worktree');p.add_argument('--verify-only',action='store_true');p.add_argument('--init-git',action='store_true');a=p.parse_args()
base=pathlib.Path(__file__).resolve().parent;repo=base.parent
m=json.loads((base/'manifest.json').read_text());dest=pathlib.Path(a.output).resolve()
if not a.verify_only and dest.exists() and any(dest.iterdir()):raise SystemExit('Refusing to replace non-empty output: '+str(dest))
with tempfile.TemporaryDirectory(prefix='market-heat-restore-') as tmp:
 arc=pathlib.Path(tmp)/'source.tar.xz';h=hashlib.sha256();n=0
 with arc.open('wb') as out:
  for part in m['parts']:
   src=(repo/part['path']).resolve()
   if not src.is_relative_to(repo):raise SystemExit('Unsafe part path')
   b=src.read_bytes()
   if len(b)!=part['bytes'] or hashlib.sha256(b).hexdigest()!=part['sha256']:raise SystemExit('Part verification failed: '+part['path'])
   out.write(b);h.update(b);n+=len(b)
 if h.hexdigest()!=m['archive']['sha256'] or n!=m['archive']['bytes']:raise SystemExit('Archive verification failed')
 expected={x['path']:x for x in m['files']};seen=set()
 with tarfile.open(arc,'r:xz') as tar:
  for member in tar:
   name=member.name;q=pathlib.PurePosixPath(name)
   if q.is_absolute() or '..' in q.parts or not member.isfile() or name not in expected or name in seen:raise SystemExit('Unexpected archive member: '+name)
   b=tar.extractfile(member).read();e=expected[name]
   if len(b)!=e['bytes'] or hashlib.sha256(b).hexdigest()!=e['sha256']:raise SystemExit('File verification failed: '+name)
   seen.add(name)
   if not a.verify_only:
    target=pathlib.Path(tmp)/'extracted'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b);target.chmod(member.mode&0o777)
 if seen!=set(expected):raise SystemExit('Missing archive members')
 if not a.verify_only:
  if dest.exists():dest.rmdir()
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(pathlib.Path(tmp)/'extracted'),str(dest))
 if a.init_git and not a.verify_only:
  subprocess.run(['git','init','--quiet',str(dest)],check=True)
  subprocess.run(['git','add','--all'],cwd=dest,check=True)
  subprocess.run(['git','-c','user.name=Market Heat snapshot restore','-c','user.email=snapshot@localhost','commit','--quiet','-m','Restore public handoff snapshot; original source '+m['sourceCommit']],cwd=dest,check=True)
 print(json.dumps({'verifiedFiles':len(seen),'sourceCommit':m['sourceCommit'],'output':None if a.verify_only else str(dest),'sanitizedFiles':m['sanitizedFiles']}))
