from langchain_core.prompts import ChatPromptTemplate



def extract_claims_prompt():
    """This function returns the prompt for extracting claims from text."""


    system_prompt = """
You are a professional in extracting facts from a document.
You will be given a document and your task is to extract ONLY factual, verifiable claims from text.

A valid claim is:

- A specific number, percentage, or statistic (e.g., "95 % of users prefer X")
- A date or timeline (e.g., "Founded in 2015", "By 2030")
- A financial figure (e.g., "Revenue of $2.5M", "Stock price of $150")
- A named entity fact (e.g., "Apple is the largest tech company")
- A technical specification (e.g., "Processing speed of 5GB/s")
- A comparison claim (e.g., "X is 3x faster than Y")
- Or any other fact that is objectively checkable using reliable sources and is a concrete statement, not an opinion


**RULES:**

- Do NOT include opinions, General explanations, subjective statements, or vague statements.
- Include the exact numbers, dates, and names.
- Do not hallucinate or make up claims that are not in the document.


IMPORTANT:
- Return results as a structured JSON ONLY. 
- Do not add any extra commentary.


Return format:

{{
  "claim": "...",
  "type": "Category of claim. eg: Financial, Date, Statistics, etc."
}}
"""


    human_prompt = """
Extract claims from the following document:

{input}
"""



    prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", human_prompt),
        ])

    return prompt





def get_verifier_prompt():
    """This prompt guides llm to verify claims."""
    

    system_prompt = """
You are a professional fact-checking assistant.
Your task is to verify factual claims using the provided web evidence.

Today's date is: {current_date} 

You must classify each claim into exactly ONE of the following:

- Verified: The evidence clearly supports the claim.
- Inaccurate: The claim is partially correct, outdated, or has incorrect details.
- False: The evidence contradicts the claim or no reliable evidence exists.


**RULES:**

- Strictly base your decision using ONLY the given evidence.
- Do not use prior knowledge.
- Do not hallucinate.
- If a claim is time-sensitive (models, prices, leadership, stats etc.) and the evidence does not explicitly confirm it is current, mark it as Inaccurate (Possibly outdated).

Return output in a structured JSON ONLY.

**RETURN FORMAT**

{{
  "claim": "...",
  "verdict": "Verified | Inaccurate | False"
}}
"""



    human_prompt = """
CLAIM:
{claim}


WEB EVIDENCE:
{evidence}
"""



    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt),
    ])

    return prompt