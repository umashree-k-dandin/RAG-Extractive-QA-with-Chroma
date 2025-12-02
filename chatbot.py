import os
import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, Docx2txtLoader, PyMuPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import pipeline
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)



# ---------------------------
# 1. Paths
# ---------------------------
DOCS_FOLDER = r"path/to/your/documents"
DB_DIR = "chroma_store"

# ---------------------------
# 2. Load documents
# ---------------------------
def load_documents(folder_path):
    docs = []
    for file in glob.glob(os.path.join(folder_path, "*")):
        if file.endswith(".pdf"):
            docs.extend(PyMuPDFLoader(file).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(file).load())
        elif file.endswith(".docx"):
            docs.extend(Docx2txtLoader(file).load())
    return docs

documents = load_documents(DOCS_FOLDER)

if not documents:
    raise ValueError(f"No documents found in {DOCS_FOLDER}")

print(f"✅ Loaded {len(documents)} documents")

# ---------------------------
# 3. Split into chunks
# ---------------------------
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

print(f"✅ Split into {len(docs)} chunks")

# ---------------------------
# 4. Embeddings
# ---------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ---------------------------
# 5. Store in ChromaDB
# ---------------------------
vectordb = Chroma.from_documents(docs, embeddings, persist_directory=DB_DIR)
retriever = vectordb.as_retriever(search_kwargs={"k": 4})  # top 5 chunks

print("✅ Vector DB created and retriever ready")

# ---------------------------
# 6. Extractive QA Model
# ---------------------------
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

print("✅ Extractive QA Model loaded")

# ---------------------------
# 7. Interactive QA Loop
# ---------------------------
while True:
    query = input("\nAsk a question (or 'exit'): ")
    if query.lower() == "exit":
        break
    
    # Retrieve top documents
    retrieved_docs = retriever.invoke(query)
    
    if not retrieved_docs:
        print("\n⚠️ No relevant context found in documents.")
        continue
    
    # Merge all retrieved chunks
    context = " ".join([doc.page_content for doc in retrieved_docs])
    
    # Run extractive QA to get concise answer
    exact_answer = qa_model(question=query, context=context)
    
    print("\n💡 Extractive Answer (precise):", exact_answer["answer"])
    print("📊 Confidence:", round(exact_answer["score"], 3))
    
    # Show all retrieved chunks for detailed context
    print("\n📝 Detailed Context from documents:")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"\n--- Chunk {i} (Source: {doc.metadata.get('source','Unknown')}) ---")
        print(doc.page_content[:1000])  # show first 1000 chars
    
    print("\n📚 Sources used:")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"   {i}. {doc.metadata.get('source','Unknown')}")
