import json
import uuid

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from alpnet.config.settings import Settings, get_settings
from alpnet.models.api import ChatRequest
from alpnet.services.llm_service import LLMService

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/rag")
async def rag_chat(
    request: ChatRequest,
    settings: Settings = Depends(get_settings),
) -> StreamingResponse:
    llm = LLMService(settings)
    conversation_id = request.conversation_id or str(uuid.uuid4())

    async def event_stream():
        yield f"data: {json.dumps({'type': 'meta', 'conversation_id': conversation_id})}\n\n"
        async for token in llm.stream_answer(request.message, context=""):
            yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
