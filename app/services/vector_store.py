from typing import List
from app.schemas import RetrievedContext


class VectorStore:
    """Placeholder vector store.

    Replace this with Pinecone, FAISS, ChromaDB, Weaviate, or another
    vector database in a production implementation.
    """

    def search(self, query: str, top_k: int = 5) -> List[RetrievedContext]:
        return [
            RetrievedContext(
                source="sample_policy_document.txt",
                content=(
                    "This is placeholder retrieved context from vector search. "
                    "In production, this would be returned from semantic similarity search."
                ),
                score=0.91,
            )
        ][:top_k]
