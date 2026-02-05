The project is not finished at all right now i do not have that much data but i will get much more on Cloud and cloud engineering. Also feel free to use clone this repo and dlete the DATA inside and put your own

# 🤖 Personal Cloud Support Assistant

A local AI-powered knowledge base that answers your cloud computing questions using your own curated documentation.

## What is this?

This is your personal **RAG (Retrieval-Augmented Generation)** system that acts like having your own cloud support engineer available 24/7. Instead of searching through documentation or waiting for support tickets, just ask questions in plain English and get accurate, sourced answers instantly.

## How it works

```
Your Documents →  Vector Database →  Local AI → 💬 Accurate Answers
```

1. **Add your knowledge** - Drop markdown or PDF files into the `data/` folder
2. **Index them** - Run `fill_db.py` to store documents in a vector database
3. **Ask anything** - Run `ask.py` and chat with your knowledge base

## Features

-  **100% Free** - Uses Ollama (local AI), no API costs
-  **Private** - Everything runs on your machine, no data leaves your computer
-  **Your Knowledge** - Answers come only from your documents, not internet hallucinations
-  **Source Citations** - Always tells you where the answer came from
-  **Fast** - Instant responses, no waiting for cloud APIs

## Current Knowledge Base

- **Azure Fundamentals** - Core Azure concepts, services, and terminology
- **Serverless Functions** - AWS Lambda, Azure Functions, and serverless architecture

## Quick Start

```bash
# 1. Activate environment
source .venv/bin/activate

# 2. Add/update documents in data/ folder, then index them
python fill_db.py

# 3. Ask questions!
python ask.py
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Vector Database | ChromaDB |
| Local LLM | Ollama (Llama 3.2) |
| Document Processing | LangChain |
| Language | Python 3.13 |

## Add More Knowledge

Simply add `.md` or `.pdf` files to the `data/` folder and run:

```bash
python fill_db.py
```

Your assistant now knows everything in those documents!

---

*Built for learning cloud concepts faster* ☁️
