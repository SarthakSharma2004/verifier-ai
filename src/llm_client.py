import os
from langchain_groq import ChatGroq


def get_llm_client():
    llm = ChatGroq(
        model = "openai/gpt-oss-120b",
        api_key = os.getenv("OPENAI_API_KEY"),
    )

    return llm