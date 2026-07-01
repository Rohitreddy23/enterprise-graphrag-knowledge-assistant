# Enterprise GraphRAG Knowledge Assistant

A production-style GraphRAG knowledge assistant that combines vector search, knowledge graphs, and LLM workflows to support enterprise document search, question answering, and knowledge discovery.

## Problem

Enterprise users often spend significant time searching across large document collections. Traditional keyword search may miss relevant context, while vector-only RAG can struggle with multi-hop questions and relationship-heavy data.

## Solution

This project uses a GraphRAG architecture that combines document embeddings, vector search, and Neo4j knowledge graph traversal. Retrieved context is passed into an LLM workflow orchestrated with LangGraph to generate grounded and explainable answers.

## Architecture

```text
Documents
   |
   v
Document Loader
   |
   v
Chunking + Metadata Extraction
   |
   v
Embeddings
   |
   +--------------------+
   |                    |
   v                    v
Vector Database       Neo4j Knowledge Graph
   |                    |
   +---------+----------+
             |
             v
Hybrid Retriever
             |
             v
LangGraph Workflow
             |
             v
LLM Response
             |
             v
FastAPI Endpoint


Tech Stack
Python
FastAPI
LangChain
LangGraph
GPT-4o
Neo4j
Pinecone
FAISS
Docker
MLflow

Key Features
Document ingestion pipeline
Chunking and metadata extraction
Embedding generation
Vector search
Knowledge graph traversal
Hybrid retrieval
LLM answer generation
FastAPI backend
Evaluation and monitoring support

Sample Use Cases
Enterprise document search
Question answering over internal knowledge
Document summarization
Policy and compliance search
Knowledge discovery across connected documents

Future Improvements
Add authentication
Add frontend dashboard
Add RAG evaluation metrics
Add latency and cost monitoring
Add support for additional LLM providers
