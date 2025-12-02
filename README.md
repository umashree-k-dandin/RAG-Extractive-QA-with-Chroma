# RAG-Extractive-QA-with-Chroma
A Retrieval-Augmented Question Answering (RAG) system using ChromaDB, HuggingFace embeddings, and DistilBERT-based extractive QA for querying PDF, TXT, and DOCX documents.



🚀 Features

📂 Load PDF, DOCX, and TXT documents

✂️ Automatically split documents into manageable chunks

🔍 Generate vector embeddings using all-MiniLM-L6-v2

🧠 Store vectors in ChromaDB for fast retrieval

🤖 Extractive QA using distilbert-base-cased-distilled-squad

💬 Interactive terminal-based question answering

📚 Displays retrieved chunks + confidence score


🛠️ Tech Stack

Python 3.x

LangChain Components

HuggingFace Transformers

Sentence Transformers

ChromaDB

PyMuPDF

Docx2Txt

📁 Project Structure
project/
│
├── data/
│   └── knowledge_base/        # Your PDFs, DOCX, TXT files
│
├── chroma_store/              # Auto-generated vector DB
│
├── main.py                    # RAG + QA pipeline
│
└── README.md


How It Works

Loads all documents from your folder path

Splits them into 1000-character chunks

Converts chunks into vector embeddings

Saves them in ChromaDB

Retrieves top-k relevant chunks when a question is asked

Sends merged context to an extractive QA model

Returns:

Precise answer

Confidence score

Retrieved document snippets

Sources


Running the App
1. Install dependencies
   pip install langchain-text-splitters langchain-community langchain-huggingface chromadb transformers pymupdf python-docx

2. Update the document folder path
In the script:
DOCS_FOLDER = r"path/to/your/documents"

3. Run the script
python main.py

4. Ask questions
Example:
Ask a question: What is the UPSC exam pattern?


Sample Output
💡 Extractive Answer (precise): The UPSC exam consists of...
📊 Confidence: 0.86

📝 Detailed Context:
--- Chunk 1 (source: upsc.pdf) ---
"The UPSC Civil Services Examination..."

