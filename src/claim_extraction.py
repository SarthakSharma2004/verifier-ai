from src.prompts import extract_claims_prompt
from src.ingestion import load_pdf
from langchain_core.documents import Document
from src.llm_client import get_llm_client

from langchain_core.output_parsers import JsonOutputParser

def extract_claim(docs : list[Document]) -> list[dict]:
    """
    Takes a list of LangChain Document objects
    and returns a list of extracted claims (JSON).
    """

    full_text = "\n".join([doc.page_content for doc in docs])

    llm = get_llm_client()
    prompt = extract_claims_prompt()
    parser = JsonOutputParser()

    chain = llm | prompt | parser

    result = chain.invoke({"input" : full_text})

    return result
   
