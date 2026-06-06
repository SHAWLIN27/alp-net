from collections.abc import AsyncIterator

from openai import AsyncOpenAI

from alpnet.config.settings import Settings


class LLMService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = AsyncOpenAI(
            api_key=settings.deepseek_api_key,
            base_url=settings.deepseek_base_url,
        )

    async def generate_answer(self, question: str, context: str = "") -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are ALP_Net, an expert A-Level Physics tutor. "
                    "Answer clearly, cite formulas using LaTeX, and ground your answer in the provided context."
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}",
            },
        ]
        response = await self.client.chat.completions.create(
            model=self.settings.deepseek_model,
            messages=messages,
            temperature=0.3,
        )
        return response.choices[0].message.content or ""

    async def stream_answer(self, question: str, context: str = "") -> AsyncIterator[str]:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are ALP_Net, an expert A-Level Physics tutor. "
                    "Answer clearly, cite formulas using LaTeX, and ground your answer in the provided context."
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}",
            },
        ]
        stream = await self.client.chat.completions.create(
            model=self.settings.deepseek_model,
            messages=messages,
            temperature=0.3,
            stream=True,
        )
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                yield content
