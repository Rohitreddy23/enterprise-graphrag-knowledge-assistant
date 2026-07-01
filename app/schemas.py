from pydantic import BaseModel, Field
from typing import List, Optional


class AskRequest(BaseModel):
    question: str = Field(..., description="User question over enterprise documents")
    top_k: int = Field(default=5, description="Number of relevant chunks to retrieve")


class RetrievedContext(BaseModel):
    source: str
    content: str
    score: Optional[float] = None


class AskResponse(BaseModel):
    question: str
    answer: str
    retrieved_context: List[RetrievedContext]


class SummarizeRequest(BaseModel):
    text: str = Field(..., description="Text to summarize")


class SummarizeResponse(BaseModel):
    summary: str
