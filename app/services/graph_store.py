from typing import List
from app.schemas import RetrievedContext


class GraphStore:
    """Placeholder graph store.

    Replace this with Neo4j queries for entity and relationship traversal.
    """

    def traverse(self, query: str) -> List[RetrievedContext]:
        return [
            RetrievedContext(
                source="neo4j_graph_context",
                content=(
                    "This is placeholder graph context. In production, this would include "
                    "entities and relationships retrieved from a Neo4j knowledge graph."
                ),
                score=0.88,
            )
        ]
