# Support Ticket Classifier

AI-powered support ticket classification service that combines rule-based heuristics, a trained scikit-learn ML model, and an LLM fallback to categorise incoming tickets by **category**, **priority**, and **sentiment**.

## Project Structure

```
support-ticket-classifier/
├── app/
│   ├── __init__.py          # Package init
│   ├── main.py              # FastAPI application entrypoint
│   ├── classifier.py        # ML-based classification logic
│   ├── rules.py             # Rule-based heuristics (keyword/regex)
│   ├── llm_fallback.py      # LLM zero-shot fallback classifier
│   └── schemas.py           # Pydantic request/response models
├── data/
│   ├── raw/                 # Raw support ticket data
│   └── processed/           # Cleaned & feature-engineered data
├── models/                  # Serialised trained models (.pkl)
├── scripts/
│   ├── prepare_dataset.py   # Data cleaning & preparation
│   └── train_model.py       # Model training & evaluation
├── tests/
│   └── test_classifier.py   # Unit & integration tests
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md
```

## Quick Start

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy environment config
cp .env.example .env
# Edit .env with your API keys

# 4. Run the development server
uvicorn app.main:app --reload
```

## Scripts

```bash
# Prepare the dataset
python -m scripts.prepare_dataset

# Train the model
python -m scripts.train_model
```

## Testing

```bash
pytest tests/
```

## Docker

```bash
docker build -t support-ticket-classifier .
docker run -p 8000:8000 --env-file .env support-ticket-classifier
```

## Known Limitations & Ambiguity

There is a documented ambiguity ceiling in the dataset regarding ticket categories, particularly between `Technical Issue` and `Account`. Many tickets contain symptoms or descriptions that straddle both categories (e.g., VPN issues or database syncs labelled as "Account"). Rather than over-tuning the model for minor accuracy gains, we use `LinearSVC` with balanced class weights as our best generalisation baseline and acknowledge the noisy ground truth.

## Tech Stack

- **API**: FastAPI + Uvicorn
- **ML**: scikit-learn, pandas, joblib
- **LLM**: OpenAI API
- **Validation**: Pydantic
- **Testing**: pytest
