# Market Heat

台灣、美國、日本公司營運與產業新聞的公開 GitHub Pages 入口。

- GitHub Pages：https://city2243.github.io/market-heat/
- 原 Sites：https://market-heat-jaime.jaime2243.chatgpt.site

## 雙站同步

既有新聞更新任務會在同一輪：

1. 收錄、核對、翻譯並更新新聞、報價、熱度與研究資料。
2. 建置及發布原 Sites 網站。
3. 更新本儲存庫的公開入口狀態，觸發 GitHub Pages 部署。
4. 兩邊分別確認部署結果；任一失敗都會如實回報。

`index.html` 嵌入原 Sites 的即時頁面，因此 GitHub Pages 讀者會看到相同內容。這保留原站的 D1、立即更新、`/api/update`、`/api/news` 與 `/api/quotes`；GitHub Pages 本身只提供靜態公開入口，不複製後端或密鑰。

## 部署

GitHub Pages 從 `main` 分支根目錄發布。每輪更新入口的資料截止狀態後，由 GitHub Pages 自動部署。

## 安全與限制

此公開儲存庫不包含登入資訊、API 密鑰、原站私有設定、n8n 秘密或後端憑證。新聞時間以頁內原始出版時間與資料截止時間為準；GitHub 提交或部署時間不等於新聞出版時間。
