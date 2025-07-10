import requests

# APIの情報を設定
api_key = "あなたのDifyのAPIキー"
api_url = "https://api.dify.ai/v1/chat-messages"

# ヘッダー情報を設定
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 無限ループで会話を開始
while True:
    # ユーザーからの入力を受け付ける
    user_message = input("あなた：")

    # 'exit'と入力されたらループを終了
    if user_message == "exit":
        print("会話を終了します。")
        break

    # Difyに送信するデータを設定
    data = {
        "inputs": {},
        "query": user_message,
        "user": "my-first-user",
        "response_mode": "blocking"
    }

    # APIを呼び出す
    response = requests.post(api_url, headers=headers, json=data)

    # 応答からAIのメッセージを取り出して表示
    # 【注意】DifyのAPI仕様により、キーの階層が異なる場合があります。
    # 実際の応答JSONを確認し、適切なキーを指定してください。
    # ここでは仮に 'answer' としています。
    ai_message = response.json()['answer']
    print(f"AI面接官：{ai_message}")