from typing import List
from app.schemas import RetrievedContext


class LLMService:
    """LLM service placeholder.

    This class is intentionally provider-neutral. In production, connect it
    to GPT-4o, AWS Bedrock, Gemini, Llama, or another model provider.
    """

    def generate_answer(self, question: str, context: List[RetrievedContext]) -> str:
        context_summary = " ".join([item.content for item in context])

        return (
            "This is a sample GraphRAG response. "
            "In production, the retrieved vector and graph context would be sent to an LLM "
            "to generate a grounded answer. "
            f"Question: {question}. Retrieved context preview: {context_summary[:250]}"
        )

    def summarize(self, text: str) -> str:
        return (
            "This is a sample summary. In production, this endpoint would use an LLM "
            f"to summarize the input text. Preview: {text[:250]}"
        )
