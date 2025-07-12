from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser



def get_rag_response(question, vector_store, openai_api_key):
  # Retrieverの作成
  retriever = vector_store.as_retriever()


  # RunableParallelで、結果を辞書としてまとめるための準備
  setup = RunnableParallel(
    context=retriever,
    question=RunnablePassthrough()
  )


  # プロンプトテンプレートの作成
  template = """
  以下の情報だけを元に、ユーザーの質問に答えてください。

  情報：
  {context}

  質問：
  {question}
  """
  prompt = ChatPromptTemplate.from_template(template)


  # Chatモデルと出力Parser（出力形式を整えるメソッド）を定義
  model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)
  parser = StrOutputParser()


  # LECLで操作をチェインする
  rag_chain = setup | prompt | model | parser


  # RAGチェインを実行して、結果を返す
  response = rag_chain.invoke(question)


  return response