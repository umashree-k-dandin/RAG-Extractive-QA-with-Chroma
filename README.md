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
