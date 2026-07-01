# Architecture Notes

## Goal

The goal of this project is to demonstrate a production-style GraphRAG architecture for enterprise document search and question answering.

## Main Components

### 1. Document Loader

Responsible for reading enterprise documents from a local folder, cloud storage, or document management system.

### 2. Chunking Service

Splits long documents into smaller chunks with metadata. Good chunking improves retrieval quality.

### 3. Vector Store

Stores embeddings for semantic search. This project includes a placeholder interface that can be connected to Pinecone, FAISS, ChromaDB, or another vector database.

### 4. Knowledge Graph

Stores entities and relationships extracted from documents. Neo4j can be used in a production implementation.

### 5. Hybrid Retriever

Combines vector search and graph traversal to retrieve more contextual and explainable information.

### 6. LLM Service

Generates answers using retrieved context. The design can support GPT-4o, AWS Bedrock, Gemini, Llama, or other model providers.

### 7. FastAPI Layer

Exposes the GraphRAG workflow through API endpoints.

## Why GraphRAG?

Vector-only RAG is useful for semantic similarity, but it can struggle with questions that require relationship awareness. GraphRAG improves retrieval by combining semantic search with entity and relationship traversal.
