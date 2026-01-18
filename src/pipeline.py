from src.ingestion import load_pdf
from src.claim_extraction import extract_claim
from src.verifier import verify_claims



def orchestrator(file_path: str):
    """This function orchestrates all the modules."""

    docs = load_pdf(file_path)

    claims = extract_claim(docs)

    verified_claims = verify_claims(claims)

    return verified_claims