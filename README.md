# FastAPI Gemini Line Bot

本專案是一個使用 FastAPI 實現的 Line Bot，並整合了 Gemini API 以提供常見問題集的答案。
請見我的 [medium](<https://medium.com/@harry12345345/%E5%B0%87%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E9%9B%86-faq-%E8%AE%8A%E6%88%90%E5%85%8D%E8%B2%BBgemini-line-bot%E6%A9%9F%E5%99%A8%E4%BA%BA-%E7%94%A8zeabur%E5%B0%87fastapi%E9%83%A8%E5%B1%AC%E5%9C%A8aws%E4%BC%BA%E6%9C%8D%E5%99%A8%E4%B8%8A-61a1f60b9243>) 

## 功能

- **FastAPI 框架**：使用 FastAPI 框架構建機器人。
- **Gemini API 整合**：從 Gemini API 獲取模型回應。
- **Line Messaging API**：通過 Line Messaging API 與用戶交流。

## 環境需求

- Python 3.7+
- FastAPI
- Uvicorn
- Line-Bot-SDK

## 安裝

1. 克隆此倉庫：
    ```sh
    git clone https://github.com/YUNHAN-LU/fastapi-gemini-linebot
    cd fastapi-gemini-linebot
    ```

2. 安裝依賴：
    ```sh
    pip install -r requirements.txt
    ```

## 運行機器人

1. 設置 Gemini 和 Line API 金鑰的環境變量。
2. 使用 Uvicorn 啟動 FastAPI 服務器：
    ```sh
    uvicorn main:app --reload
    ```

## 使用方法

- 通過 Line 應用與客服機器人溝通。

## 專案結構

- **api/**：包含 API 路由定義。
- **resource/**：包括配置和工具文件。
- **main.py**：FastAPI 應用的主入口。

