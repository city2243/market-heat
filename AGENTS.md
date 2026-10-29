# Codex 接手 Market Heat

先讀 `docs/CODEX_HANDOFF.md`、`handoff/STATUS.json`。這個儲存庫同時保存公開 Pages 入口與完整公開研究/程式快照。**不要只修改入口就稱研究完成。**

## 恢復工作目錄

```bash
python3 handoff/restore.py --verify-only
python3 handoff/restore.py --output worktree --init-git
cd worktree
npm run install:ci
node scripts/census-workflow.mjs refresh
node scripts/census-workflow.mjs plan --limit 20
```

若 worktree 已有內容，直接檢查已保存狀態，不要覆蓋或刪除。read `UPDATE.md`、`QUALITY_GOALS.md`、`RESEARCH_DESK.md`、`docs/census-updates.md`、`docs/chinese-reading.md`、`docs/catalysts.md`。現況數字從journal重算。

## 不可違反

- 每家公司七項公開原始證據齊備且有效才complete。只列計畫、開入口、候選或測試通過不算。
- 完成一批後接續下一批；當期母體全完成才轉90天維護。過期契約要逐筆續約/清償證據，不推定。
- 私有LINE僅線索，不將私人原文/網址/定位、密鑰或憑證提交此公開儲存庫。Runtime secrets留原Sites。
- 今日新聞按台北原始出版日；不重標舊資料日期。保存不可變快照、raw與凍結驗證資料。
- 每輪可部分發布，但必須實報來源/翻譯/品質缺口與真正部署結果，不下修驗證。
- 原Sites project_id固定 appgprj_6aa0e3f948988191875bab0b452dfdca；保持目前公開權限，不另建站。
- GitHub Pages仍為main根目錄靜態入口，後端/D1/更新API仍在原Sites。
- 既有每日六個台北時段任務不新增、不重建。交接不代表既有任務自動停止；避免同批雙writer。
- 維持data/census不可變journal與apply/close/refresh；最新實質證據先保存，才能報進度。

本快照不含Git歷史物件或執行期授權。正式部署先依Sites技能取得原來源及既有授權；新研究要提交原來源並更新公開快照/manifest，別只留在被gitignore的worktree。原站只有terminal succeeded，Pages只有讀回本輪marker，才各自可稱成功。交接文件內所有歷史數字不是新一期收錄截止。
