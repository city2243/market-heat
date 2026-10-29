# Market Heat：研究與維護完整交接

交接日期：2026-10-29。這是可接續的工作狀態與操作規格，**普查尚未完成**。使用者已授權原站持續發布、公開 GitHub 交接及雙站更新。最新明確指示優先於 UPDATE.md 中較舊段落。

## 1. 接手先做

1. GitHub 根目錄讀 `AGENTS.md`、本文件及 `handoff/STATUS.json`。
2. 執行 `python3 handoff/restore.py --output /workspace/sites/market-heat --init-git`，或指定另一個空目錄。驗證所有分片及還原檔 SHA-256；已有資料的目錄不得覆蓋。`--init-git`建立獨立本機快照提交，供歷史overlay保護檢查辨識既有檔案；此合成提交不是原Sites來源SHA，不能強推至原站。資料包含程式、設定範本、公開研究、raw、snapshots、latest、index、不可變歷史與測試；不含 Git 物件、node_modules、建置產物、私密研究與執行期秘密。
3. 在還原目錄依序讀 `UPDATE.md`、`QUALITY_GOALS.md`、`RESEARCH_DESK.md`、`docs/census-updates.md`、`docs/chinese-reading.md`、`docs/catalysts.md`。讀 `data/census/status.json` 與完成目標，不使用本文件寫死的數字代替實際重算。
4. 原 Sites 來源分支仍是正式部署來源。若有 Sites 連接能力，讀 Sites 技能、成功 get_site，再取得該站短效 repository credential 更新原來源。先保留交接後新增證據，不能用舊遠端覆寫交接內容或強推。GitHub archive 是此交接時點備份，不是原站憑證。
5. 恢復依賴、refresh/QC，先接續未結束批次，否則 `plan --limit 20`。每家公司實讀後即 apply，不等整批最後才保存。接著逐批推進；任何一次發布均不代表全體普查完成。

## 2. 目標與可核對現況

當期官方普通股母體為 **1,994 家**（上市1,098、上櫃896；名冊出表1151028），不可固定舊1,990。當期全母體每家七項已查、證據有效，才可宣布首次普查完成；之後90天複查、新上市櫃加入、下市移除但保留歷史。

此批 `2026-10-29T09-45-41-472Z-9d9a28` 已20家 apply/close/refresh：新增11家完整、131項；累計 **234/1,994家、2,729/13,958項，仍1,760家不完整**。processed只表示有保存，並非complete。詳細狀態及每項公開來源在 data/census、data/company-link-census.json。

本批完整：2375、3272、5285、5324、5905、6136、6906、7791、7821、8349、8367。
本批仍缺currentValidity：3576、3685、4139、4588、6655、6697、6887、7782、8067。逐筆到期融資、租約、授權或供貨契約未證實續約/清償，不可由當期總收入、總借款或租金推定全部有效。具體原約、期限及下一來源列於 `data/census/progress-20261029-handoff.json`。
前批5706責任險及6873融資/CPD/替約仍待查。5706觀光署已讀到的是履約保證險，不足以證明另一責任險已續保。

新聞最近已核截止 **2026-10-29 17:05:00 台北**，edition=`2026-10-29T16-59-35`，台美日讀者可見各10。研究/交接時間不得冒充新收錄時間。最新已部署結果以 handoff/STATUS.json 為準，別把本檔提交當原站成功部署。

## 3. 七項證據普查（完成標準不能降低）

每家固定七項鍵：annualReport、officialRelations、productAndPaymentPath、currentValidity、conflictsAndCounterevidence、materiality、officialEventCalendar。

- 實讀公開年報/完整法說營運、產品、客戶集中、重要契約及最新財報；只讀入口、檔名或搜尋摘要不算完成。
- 逐跳辨識具名客戶、供應商、IP、股權及替代關係。認證、同業、共同老闆、投資持股、平台相容，不等於已證供應訂單；匿名客戶不猜名。
- 區分產品、零件、交付及付款主體，預收/合約負債不當營收，處分資產不當本業轉盈。
- 查到期、終止、不續租、替約、分單、減損、訴訟及反證；財報與法說有矛盾要同存，不抹去。
- 量化收入/毛利敏感度僅用已讀證據；未知不編估。美股EPS超預期不自動推台股受惠。
- 官方行程保留原日期精度；沒有明印時區就待確認。沒有未來行程可記限於已查來源未找到，不能偽造行程。

每項保存 status/outcome/conclusion/evidence/searches/limitation；evidence每筆含 url/title/publishedAt/accessedAt/locator/observation。日期未知=null；observations是自己的簡短摘要，不是搬運全文。全部七項reviewed且在有效期內才complete。未揭露可作限於已讀文件的結論，但未讀、取件失敗、待確認不能改成未揭露。

```bash
node scripts/census-workflow.mjs refresh
node scripts/census-workflow.mjs plan --limit 20
node scripts/census-workflow.mjs apply --run <實際run-id> --reviews <公開證據JSON>
node scripts/census-workflow.mjs close --run <實際run-id> --note '<實際完整家數/項數與限制>'
node scripts/census-workflow.mjs refresh
node scripts/build-census-qc.mjs
```

apply以指紋產生不可變journal，同一內容重送不重計。補件新增review，不改舊journal；更新reviewedAt為真實查核時刻。單writer，保留lock；崩潰先確認原PID不存在再恢復。每批保存後繼續可取得證據的公司，受阻換公司官網、MOPS原始PDF/XBRL、對手公告、主管機關，不只重跑連線。若新增完整0家，必須記具體原因及不同替代來源。

官方MOPS取件方式已詳列 docs/census-updates.md：先索引取得真檔名再取PDF，不猜路徑；掃描PDF用影像核對。下載成功不是實讀完成，限流不要密集重試，也不要繞過存取限制。

## 4. 私人研究與公開資料界線

使用者既有LINE產業研究資料庫只供內部找線索，再用公開官方來源驗證。接手者需透過使用者授權的Google Drive/LINE連接自行找原庫；此公開交接不提供私人文件ID、列號、原文、網址或券商內文。

本輪曾發現摘要與同列原文不相符，已按內容識別與原資料日期找到對應原文。以後不能只信列號；無法核對就揭露範圍，不宣稱已完成私人庫增量同步。含模型整理的題材圖只能作候選，不能當供應關係證據。

官方公告屬公司自述，不當獨立第三方證據。引用公司官方公開Drive附件須確認來自官方網站，不能混入使用者私人Drive。

## 5. 每輪新聞、翻譯、報價與熱度

最新今日閱讀規則優先：預設清單、大家在看、美股補充與related均依**台北當天原始出版日**篩選。24h歷史聯集保留，但舊內容僅主動選歷史可見；不以昨天仍在24h內的文章補今日十則。updated-only不能冒充新事件，日期未確認不能混入。日期只有日則保留精度，不補造時間。

```bash
python scripts/collect-news.py
# 實讀來源/擴大原文補查、去重、公司校正、寫稽核和繁中reason/翻譯
python scripts/collect-quotes.py
node scripts/build-heat.mjs
node scripts/build-hot24-history.mjs
python scripts/test-industry-rules.py
node tests/news-fallback.test.mjs
node tests/news-update.test.mjs
python scripts/check-translations.py
node --test tests/heat-engine.test.mjs
node scripts/check-current-edition.mjs
node scripts/validate-quality.mjs
npm run build
```

查詢/直接來源以data/news-config.json、scripts/industry_rules.py、data/source-feeds.json為準；Google失敗Bing備援，直接來源獨立抓取。美股優先英文Newsroom/IR，日股日文公告、EE Times Japan、MONOist與當地媒體。不足持續跨公司跨產業補搜，不用舊聞湊；原文日期/公司/事件與原始收錄稽核必須可查。全部來源失敗僅重試一次，保留上一期日期。

只留可辨識上市公司的訂單、供需、產能、成本/報價、capex、產品技術、合作併購、營收財報與直接公司法規。排除股價、估值、投資建議、籌碼、ETF、配息、泛總經、導購及通用名單。原精選清單每家公司主題最多一則；此限制不套用所有合格觀測/熱門事件。

每companies[]具繁中reason，說明具體角色及證據，跨市填market；保留傳聞/計畫/量產狀態。報價含幣別/市場/時間/來源，漲跌對前收；失敗保留帶日期舊值或缺值，不能填0。歷史新聞顯示最新可得價，不當事件當時價，也不歸因新聞。

完整標題翻譯涵蓋observations/news/related/跨期保留/研究候選/排除清單，原標題為data/translations/zh-Hant.json的鍵，保留數字型號與不確定語氣；截斷標示原標題截斷。標題翻譯不等於全文查核，不能補寫未讀正文。勿更動matching-translations的凍結分析特徵。政策變更需同步Python/config/TypeScript並執行export-news-config.py。

熱度全合格observations為母體，追加搜尋queryPurpose=event-followup、追加feed purpose=event-followup，不能進固定panel歷史基準。hot24依現行lib/hot24-engine.mjs門檻，至少3稿源組或3網域，區分獨立稿源與廣泛轉載，不稱閱讀數。合併窗口內已保存有效觀測，同URL沿用最早出版時間。熱門議題與單一事件分開，新早期重要事件亦保留。來源少於2組不給擴散分，歷史不足維持基準累積中。

## 6. 品質與不可變研究

以現行validate-quality.mjs列出的檢查數為準；目前36組，不能沿用舊18組。保存quality-status、benchmark-results及public對應檔。測試通過不等於全市場效果達標。

v3.4已見285組都屬開發用途，53組資訊不足；追加225開發回放TP58/FP0/FN18/TN108，58/76=76.3%，日文11/16=68.75%尚未70%。原73、60及225首次結果、v3.2/v3.3凍結副本、audit-lifecycle等不改；成對公開正文僅2組，獨立人工0。不可把保留案例算答對或把開發回放稱獨立盲測。

未來協議forward-audit-protocol-v2.json，保留v1，原起點2026-09-14 08:00台北；每市場100組、每公司≤20。只新發布/新觀測固定來源，排除已見網址標題、追加搜尋和未來資訊；只追加不替換，不以模型預測作標籤。先讀兩篇原文/時間/事件，再排除開發重疊。付費牆/證據不足保留；凍結匹配程式與門檻不得調整。事後來源修正只限逐篇已核URL/標題並標版本，不增加過去固定觀測。

2026-10-19最新發布決策：每輪即使未足十則、翻譯未完或部分品質失敗，仍發布**真實且明示缺口的部分更新**，無新內容則發布狀態且保留舊日期。繼續執行檢查，保存失敗，不改標籤/門檻。真實build或部署障礙須修復、重試並誠實回報，不能稱已發布。

## 7. 催化劑與公司傳導

data/catalysts.json與不可變data/census/event-reviews同時維護。核對即將到來、延期/取消、已發生結果；實讀公告/簡報及可得逐字稿，限制逐條寫。事件自身公司與傳導對象分開，勿出現聯發科傳導至聯發科。Tesla/Musk相關xAI/SpaceX/Starlink僅觀察範圍，逐段確認法人/承諾/產品/付款/出貨，不因同老闆直接認定。

```bash
node scripts/census-workflow.mjs event-review --reviews <公開事件JSON>
node scripts/check-catalysts.mjs
```

結果impacts需覆蓋事件chainIds及ownChainIds；direction用not_mentioned/up/down/unchanged/uncertain並指向本筆證據索引。本批已另核波音、譜瑞結果，加入亞德客6筆官方後續行程；沒有明印時區則dateOnly，不硬轉時區。

## 8. 雙站、來源與排程

- 原Sites： https://market-heat-jaime.jaime2243.chatgpt.site
- project_id：`appgprj_6aa0e3f948988191875bab0b452dfdca`
- GitHub： https://github.com/city2243/market-heat ，main根目錄Pages入口。
- Pages： https://city2243.github.io/market-heat/
- 保持目前公開權限，不能被較舊私人段落改回。GitHub保持靜態入口；D1 DB、news_update/news_editions、/api/update、/api/news、/api/quotes與秘密留原Sites。
- 既有任務 `6aa0e813ab588191a0c201ccc902709c`：台北每日00:45、04:45、08:45、12:45、16:45、20:45。已啟用完成目標；不新增/重建重複任務，不啟用付費服務。接手並不自動取得此任務控制權，也不等於原任務已停。

讀Sites技能後get_site；取得短效repository credential（不寫檔、不放argv、不輸出token），原來源helper恢復checkout。依技能build→commit→push→package→save→deploy，精確來源commit及archive一致；deploy terminal succeeded才叫原站更新。保存version/deployment id與URL。曾遇Git HTTP500，以正常Git protocol.version=0、HTTP/1.1成功；這是可用相容設定，不准繞過網路限制。曾Cloudflare首次部署失敗，重試同已保存版本成功；每次仍查實際status。

原站成功後更新GitHub index.html公開sync狀態/唯一marker/真實新聞截止；保留iframe及其他內容。讀最新blob SHA再更新，勿覆寫別人提交。驗證公開Pages HTTP200且含本輪marker後才說雙站成功；任一端失敗，另一端照可行結果保存並分開回報。

Runtime只記秘密名稱與用途，不提供值：NEWS_TRANSLATE_URL為伺服器端既有n8n翻譯連接；D1 DB由Sites綁定。完整部署能力需使用者既有Sites及GitHub授權，不可從公開repo推導/取得秘密。沒有授權時先做本機研究/測試與GitHub保存，具體回報部署阻礙。

## 9. 每批報告與接續

回報新增完整公司/項目、累計/當期母體、仍缺公司及具體來源障礙、品質真實結果、新聞原截止、原站與Pages各自狀態。不要僅說「處理中」「排程已開」或「20家已處理」代替完成數。每家公司先保存、每批close/refresh，串流中斷後讀journal及Git狀態接續，不從零重做。未知錯誤原因不要猜已修復。

第一優先接續普查，尤其本批9家與前批2家逐筆到期契約；有公開Q3/重大公告就補件，無新文件則換下一跨產業批次，不讓單一來源障礙阻斷全母體進度。新聞雙站更新仍維持現行任務。完整條件達成後才轉維護，不能手動把complete設true。
