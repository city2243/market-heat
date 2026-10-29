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

快照包含現有程式、設定範本、公開研究證據與不可變資料歷史，分片只是為了可靠傳輸；還原程式驗證每一片、整包及每個檔案。`worktree/`不自動提交，防止依賴或秘密意外上傳；新結果須按交接流程同步正式來源與更新快照。沒有封存依賴、執行期秘密或私人研究原文。

## 現況

2026-10-29交接批次新增11家七項完整、131項查核；累計234/1,994家，2,729/13,958項。仍1,760家公司不完整，目標未完成。數字以交接狀態與後續journal重算為準。

新聞最近已核截止為2026-10-29 17:05台北，台美日各10則。本次研究交接時間不代表重新收錄新聞。品質回歸通過不等於全市場效果達標。

## 網站架構

main根目錄 `index.html` 仍嵌入原Sites；GitHub Pages只提供靜態入口。D1 DB、立即更新、/api/update、/api/news、/api/quotes與翻譯秘密仍由原Sites提供。不得把封存原始碼誤當已搬遷後端。兩站部署分別驗證。

既有任務保持台北00:45、04:45、08:45、12:45、16:45、20:45；沒有新增任務。Codex接手不會自動停用原任務，需沿用保存紀錄並避免並行寫入同批。
