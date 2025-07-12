from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma




class VectorStore():
  def __init__(self):
    self.chunk_size = 200
    self.chunk_overlap = 20
    self.persist_dir = "./chroma_db"


  def create(self, knowledge_path: str):
    # Textファイルを読み込む
    loader = TextLoader(knowledge_path)
    documents = loader.load()

    # ドキュメントの分割
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
    splitted_documents = text_splitter.split_documents(documents)

    # Embeddingモデルの準備
    embeddings = OpenAIEmbeddings()

    # ChromaでVector Storeの構築
    vector_store = Chroma.from_documents(
      documents=splitted_documents,
      embedding=embeddings,
      persist_directory=self.persist_dir
    )
    vector_store.persist()

    return


  def read(self):
    # Embeddingモデルの準備
    embeddings = OpenAIEmbeddings()

    # Vector Storeの読み込み
    vector_store = Chroma(
      persist_directory=self.persist_dir,
      embedding_function=embeddings
    )

    # デバッグ
    print(f"ベクトル数: {len(vector_store.get()['documents'])}")

    return vector_store