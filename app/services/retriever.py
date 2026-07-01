from typing import List
from app.schemas import RetrievedContext
from app.services.vector_store import VectorStore
from app.services.graph_store import GraphStore


class HybridRetriever:
    """Combines vector search and graph traversal for GraphRAG retrieval."""

    def __init__(self):
        self.vector_store = VectorStore()
        self.graph_store = GraphStore()

    def retrieve(self, question: str, top_k: int = 5) -> List[RetrievedContext]:
        vector_context = self.vector_store.search(question, top_k=top_k)
        graph_context = self.graph_store.traverse(question)

        combined_context = vector_context + graph_context
        return combined_context[:top_k]
