from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

loader=PyPDFLoader("data/ml_notes.pdf")
documents=loader.load()
print(f"Total Pages: {len(documents)}")
print("\nFirst Page:\n")
print(documents[0].page_content)

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks=text_splitter.split_documents(documents)
print(f"Total Pages : {len(documents)}")
print(f"Total Chunks: {len(chunks)}")
print("\nFirst Chunk:\n")
print(chunks[0].page_content)
print("\nMetadata:\n")
print(chunks[0].metadata)
print("Creating embedding model...")
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("Embedding model loaded!")

print("Creating FAISS vector database...")

vector_db = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

print("FAISS vector database created successfully!")

print("Creating retriever...")
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)
print("Retriever created!")

print("Loading LLM...")
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4.1-mini",
    max_tokens=512,
    temperature=0
)
print("LLM loaded!")
print("total chunks stored:",len(chunks))

query=input("Ask a question: ")
docs=retriever.invoke(query)
context = "\n\n".join(doc.page_content for doc in docs)
prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the context below.

If the answer is not present,
say:
"I don't know based on the provided document."

Context:

{context}

Question:
{query}
"""

response=llm.invoke(prompt)
print("\nAnswer:\n")
print(response.content)