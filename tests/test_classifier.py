import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from app.main import app
from app.rules import classify_by_rules
from app.classifier import classify_ticket

client = TestClient(app)

def test_classify_by_rules():
    assert classify_by_rules("I can't login to the system") == "Login Issue"
    assert classify_by_rules("My payment was declined") == "Payment"
    assert classify_by_rules("I need vpn authorization") == "Account"
    assert classify_by_rules("My delivery is late and tracking number doesn't work") == "Delivery"
    assert classify_by_rules("The app has a bug and crashed") == "Technical Issue"
    assert classify_by_rules("I want to buy a bulk order for enterprise plan") == "Others"
    assert classify_by_rules("Unknown random text about weather") is None

def test_classify_ticket_end_to_end():
    # 5 sample inputs: login, payment, password change, delivery, app crash
    assert classify_ticket("I can't login")["category"] == "Login Issue"
    assert classify_ticket("My payment failed")["category"] == "Payment"
    assert classify_ticket("I need a password change")["category"] == "Login Issue"
    assert classify_ticket("Where is my delivery")["category"] == "Delivery"
    assert classify_ticket("The app crash on startup")["category"] == "Technical Issue"

def test_classify_api_success():
    response = client.post("/classify", json={"text": "I can't login"})
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "confidence" in data
    assert "method" in data
    assert data["category"] == "Login Issue"

def test_classify_api_empty_text():
    response = client.post("/classify", json={"text": "   "})
    assert response.status_code == 422
    
    response2 = client.post("/classify", json={"text": ""})
    assert response2.status_code == 422

def test_classify_api_with_llm_fallback(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test_key")
    
    with patch("app.llm_fallback.openai.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(message=MagicMock(content="Technical Issue"))]
        mock_client.chat.completions.create.return_value = mock_completion
        
        with patch("app.main.classify_ticket") as mock_classify:
            mock_classify.return_value = {"category": "Others", "confidence": 0.4, "method": "ml_low_confidence"}
            
            response = client.post("/classify?fallback=llm", json={"text": "Some weird issue"})
            assert response.status_code == 200
            data = response.json()
            assert data["method"] == "llm_fallback"
            assert data["category"] == "Technical Issue"

@patch("app.main.classify_ticket")
@patch("app.main.classify_with_llm")
def test_classify_api_with_llm_fallback_error(mock_llm, mock_classify):
    mock_classify.return_value = {"category": "Others", "confidence": 0.4, "method": "ml_low_confidence"}
    mock_llm.side_effect = Exception("LLM Error")
    
    response = client.post("/classify?fallback=llm", json={"text": "Some weird issue"})
    assert response.status_code == 200
    data = response.json()
    assert data["method"] == "ml_low_confidence"
    assert data["category"] == "Others"
