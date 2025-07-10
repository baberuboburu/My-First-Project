# Dify-Streamlit-Chatbot

Difyの大規模言語モデルAPIとStreamlitを活用した、簡易かつ強力なAIチャットボットアプリケーションです。ユーザーが入力した質問に対し、リアルタイムで自然な応答を返します。  
開発初学者でも扱いやすく、学習や業務支援の第一歩として最適です。

---


## 📁 構成

```
My-First-Project/
├── app.py               # Streamlitチャットボットの実装
├── requirements.txt     # 必要ライブラリの一覧
└── README.md            # このドキュメント
```

---

## ⚙️ 使用技術

- **Python 3.11**
- **Streamlit**：Webアプリ作成フレームワーク
- **Requests**：Dify APIとの通信
- **Dify**：大規模言語モデルのバックエンドAPIプラットフォーム

---

## 💻 セットアップ手順

### 1. リポジトリのクローン

```
git clone https://github.com/baberuboburu/My-First-Project.git
cd My-First-Project
```

### 2. 仮想環境を作成・有効化（任意）

```
python -m venv .venv
source .venv/bin/activate  # Windowsなら .venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```
pip install -r requirements.txt
```


## ▶️ アプリの実行

```
streamlit run app.py
```

ブラウザが自動的に開かない場合は、 http://localhost:8501 にアクセスしてください。

---

## 💬 動作イメージ

1. ユーザーがメッセージを入力
2. Dify APIを経由してLLMにクエリ送信
3. 応答結果がチャット形式で表示

---

## 📌 注意点

- `response_mode = "blocking"` を使用しているため、応答が完了してから返されます（ストリーミング対応は未実装）。

---

## 📝 ライセンス

MIT License