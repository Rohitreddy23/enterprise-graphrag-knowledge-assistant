from fastapi import APIRouter
from app.schemas import AskRequest, AskResponse, SummarizeRequest, SummarizeResponse
from app.services.retriever import HybridRetriever
from app.services.llm_service import LLMService

router = APIRouter()

retriever = HybridRetriever()
llm_service = LLMService()


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    retrieved_context = retriever.retrieve(payload.question, top_k=payload.top_k)
    answer = llm_service.generate_answer(payload.question, retrieved_context)

    return AskResponse(
        question=payload.question,
        answer=answer,
        retrieved_context=retrieved_context,
    )


@router.post("/summarize", response_model=SummarizeResponse)
def summarize_text(payload: SummarizeRequest):
    summary = llm_service.summarize(payload.text)
    return SummarizeResponse(summary=summary)
