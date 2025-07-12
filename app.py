from vector_store import VectorStore
from functions import get_rag_response
import streamlit as st
import requests

# ベクトルストアのインスタンス化と読み込み
vector_store_instance = VectorStore()
vector_store = vector_store_instance.read()

# API Keyの取得
openai_api_key = st.secret["OPENAI_API_KEY"]




# タイトルを設定
st.title("🤖 RAGを使ったチャットボット")

# 1. 初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 履歴表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 入力と履歴追加
if prompt := st.chat_input("メッセージを送信"):
    # ユーザーの入力を保存＆表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # RAGを使った応答の生成
    ai_message = get_rag_response(prompt, vector_store, openai_api_key)

    # AIの返答を保存＆表示（オウム返し→RAGチャットボットに変更）
    st.session_state.messages.append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        st.markdown(ai_message)