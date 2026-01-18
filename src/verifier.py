from src.prompts import get_verifier_prompt
from src.llm_client import get_llm_client
from src.web_retriever import search_claim
from langchain_core.output_parsers import JsonOutputParser
from datetime import date


def verify_claims(claims: list[dict]) -> list[dict]:
    """
    Takes a list of claims (JSON), compares them with facts and returns a list of verified claims (JSON).
    """

    llm = get_llm_client()
    prompt = get_verifier_prompt()
    parser = JsonOutputParser()
    today = str(date.today())

    chain = prompt | llm | parser

    final_results = []

    for item in claims:
        claim_text = item["claim"]

        evidence = search_claim(claim_text)

        result = chain.invoke({
            "claim": claim_text,
            "evidence": evidence,
            "current_date": today
        })

        result['source'] = evidence

        final_results.append(result)

    return final_results