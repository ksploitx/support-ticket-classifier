from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from app.schemas import TicketRequest, TicketResponse
from app.classifier import classify_ticket
from app.llm_fallback import classify_with_llm

app = FastAPI(title="Support Ticket Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/classify", response_model=TicketResponse)
def classify_endpoint(request: TicketRequest, fallback: Optional[str] = Query(None)):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=422, detail="Ticket text must be non-empty.")

    result = classify_ticket(request.text)

    if result.get("method") == "ml_low_confidence" and fallback == "llm":
        try:
            llm_result = classify_with_llm(request.text)
            llm_result["method"] = "llm_fallback"
            return llm_result
        except Exception:
            # Fall back to returning the original "Others" result rather than erroring out
            pass
            
    return result
