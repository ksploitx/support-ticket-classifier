import os
import joblib
import json
from typing import Dict, Any
from app.rules import classify_by_rules

# Determine base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Load models and artifacts at module import
try:
    vectorizer = joblib.load(os.path.join(MODELS_DIR, "vectorizer.pkl"))
    model = joblib.load(os.path.join(MODELS_DIR, "model.pkl"))

    with open(os.path.join(MODELS_DIR, "labels.json"), "r") as f:
        labels = json.load(f)
except (FileNotFoundError, OSError, EOFError, ImportError, Exception) as e:
    vectorizer = None
    model = None
    labels = []

def classify_ticket(text: str, confidence_threshold: float = 0.6) -> Dict[str, Any]:
    # 1. Try classify_by_rules(text) from app.rules
    rule_category = classify_by_rules(text)
    if rule_category:
        return {"category": rule_category, "confidence": 1.0, "method": "rule"}
    
    if model is None or vectorizer is None:
        return {"category": "Others", "confidence": 0.0, "method": "error_no_model"}
    
    # 2. Otherwise, vectorize the text, run model.predict_proba
    X = vectorizer.transform([text])
    probabilities = model.predict_proba(X)[0]
    
    # Get the top category and its probability
    top_index = probabilities.argmax()
    prob = probabilities[top_index]
    top_category = labels[top_index]
    
    # 3. If probability >= confidence_threshold
    if prob >= confidence_threshold:
        return {"category": top_category, "confidence": float(prob), "method": "ml"}
    
    # 4. If probability < confidence_threshold
    return {"category": "Others", "confidence": float(prob), "method": "ml_low_confidence"}
