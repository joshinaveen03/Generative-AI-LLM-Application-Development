from dotenv import load_dotenv


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma


load_dotenv()


# 1. Load PDF
docs = PyPDFLoader("attention.pdf").load()


# 2. Split into chunks
chunks = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
).split_documents(docs)


# 3. Store chunks as embeddings
db = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(model="text-embedding-3-small")
)


# 4. Ask a question and retrieve relevant chunks
question = "what is global waarming?"
docs = db.similarity_search(question, k=3)


# 5. Give retrieved text to the LLM
context = "\n\n".join(doc.page_content for doc in docs)


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


answer = llm.invoke(
    f"""
    Answer the question using only the context below.


    Context:
    {context}


    Question:
    {question}
    """
)


print(answer.content)
 