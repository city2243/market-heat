# Market Heat — Codex 研究與維護交接

台、美、日公司營運新聞、事件熱度、台股公司關係普查與催化劑日曆。

- [Codex 接手完整說明](docs/CODEX_HANDOFF.md)
- [接手代理操作規則](AGENTS.md)
- [交接實際狀態與部署紀錄](handoff/STATUS.json)
- [完整公開快照清單與 SHA-256](handoff/manifest.json)
- [GitHub Pages](https://city2243.github.io/market-heat/)
- [原 Sites](https://market-heat-jaime.jaime2243.chatgpt.site)

## 讓 Codex 接手

把此儲存庫交給 Codex，指示：

> 先讀 AGENTS.md 與 docs/CODEX_HANDOFF.md，驗證並還原 handoff 快照，接續已保存研究。以當期全台上市櫃公司全部七項有效公開證據完成為目標，逐批 apply、close、refresh；同步維護新聞、報價、熱度、催化劑與原 Sites/GitHub Pages。不要降低標準、公開私人資料、另建網站或重複排程。回報實際新增完成數與雙站結果。

```bash
python3 handoff/restore.py --verify-only
python3 handoff/restore.py --output worktree --init-git
```

快照包含現有程式、設定範本、公開研究證據與不可變資料歷史，分片只是為了可靠傳輸；還原程式驗證每一片、整包及每個檔案。worktree/不自動提交，防止依賴或秘密意外上傳；新結果須按交接流程同步正式來源與更新快照。沒有封存依賴、執行期秘密或私人研究原文。

## 現況

新聞補充更新至 2026-11-15 10:07:47 台北時間。讀者實際可見台／美／日 2／10／5 則；台灣、日本與美股原收錄截止為 08:53:15，僅 SpaceX Starship Flight 15 追加查核至 10:07:47。上級飛船完成軌道飛行後由發射塔捕捉；Super Heavy 助推器未完成捕捉。三家媒體報導為同一事件。品質檢查 36 項中 34 項通過；未通過原因是全歷史翻譯缺口及三市場各十則未達。這不是完整市場普查。

SPCX 最新可得報價為 2026-11-13 收盤 139.11 美元，較前收 -0.83 美元（-0.59%）；不是新聞發生時價格。報價資料更新 602／607 檔。

公司普查的最後保存進度仍為 2026-10-29 交接狀態：本輪新增完整 11 家、新增核對 131 項；累計 234／1,994 家、2,729／13,958 項。公司母體與證據狀態須按最新保存的普查紀錄複核後更新；新聞更新不等於普查進度。

原 Sites v278 已成功部署；本頁是公開靜態入口並同步本期實際資料截止。原 Sites 仍提供新聞後端、D1、立即更新、/api/update、/api/news 與 /api/quotes。不要將來源觀測稱為全市場覆蓋或零漏報。

## 網站架構

main 根目錄 index.html 嵌入原 Sites；GitHub Pages 只提供靜態入口。後端與個人化功能仍由原 Sites 服務。不得把封存原始碼誤當已搬遷後端。兩站部署分別驗證。

既有任務保持台北 00:45、04:45、08:45、12:45、16:45、20:45；沒有新增任務。Codex 接手不會自動停用原任務，需沿用保存紀錄並避免並行寫入同批。
