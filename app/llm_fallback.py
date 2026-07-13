import os
import openai
from dotenv import load_dotenv

load_dotenv()

VALID_CATEGORIES = {"Login Issue", "Payment", "Account", "Delivery", "Technical Issue", "Others"}

def classify_with_llm(text: str) -> dict:
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            return {"category": "Others", "confidence": None}
            
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            timeout=5.0
        )
        
        prompt = (
            f"Classify the following support ticket into exactly one of the following categories: "
            f"Login Issue, Payment, Account, Delivery, Technical Issue, Others.\n\n"
            f"Return ONLY the category name and nothing else.\n\n"
            f"Ticket: {text}"
        )
        
        response = client.chat.completions.create(
            model="google/gemini-2.5-pro",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        
        result = response.choices[0].message.content.strip()
        
        if result in VALID_CATEGORIES:
            return {"category": result, "confidence": None}
            
        return {"category": "Others", "confidence": None}
        
    except Exception:
        return {"category": "Others", "confidence": None}
