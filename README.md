# Enterprise Knowledge Worker (RAG)

A Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over enterprise documents. The system combines semantic search, keyword search, hybrid retrieval, reranking, and LLM-based generation to provide accurate and context-aware answers with source citations.

## Features

- PDF document ingestion
- Text cleaning and preprocessing
- Intelligent document chunking
- Embedding generation using Sentence Transformers
- ChromaDB vector storage
- Semantic vector retrieval
- BM25 keyword retrieval
- Hybrid retrieval (Vector + BM25)
- Cross-Encoder reranking
- LLM-powered answer generation
- Source citation support

## Architecture

```
PDF
 ↓
Loader
 ↓
Text Cleaning
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Vector Retrieval
 ↓
BM25 Retrieval
 ↓
Hybrid Retrieval
 ↓
Cross Encoder Reranking
 ↓
Prompt Building
 ↓
LLM Generation
 ↓
Final Answer + Citations
```

## Tech Stack

- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Rank-BM25
- Hugging Face Models
- Ollama
- Mistral

## Project Structure

```text
Rag_system/
│
├── app/
│   ├── injestion/
│   │   ├── loader.py
│   │   ├── clean.py
│   │   ├── chunker.py
│   │   └── embeddings.py
│   │
│   ├── retrieval/
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── bm25_retriever.py
│   │   ├── hybrid_retrieval.py
│   │   └── reranker.py
│   │
│   └── generation/
│       ├── prompt_builder.py
│       └── generator.py
│
├── data/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Rag_system
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Example Query

```text
What is the internship duration?
```

## Example Output

```text
The internship duration is May–July 2026 (60 days).

Sources:
Page 0 | Chunk ID: xxxx
Page 1 | Chunk ID: yyyy
```

## Future Improvements

- Agentic RAG
- Query Routing
- Multi-PDF Support
- Evaluation Pipeline
- Guardrails
- Conversation Memory
- Web Search Integration
- Enterprise Knowledge Assistant

## Author

Prachi Paunikar
