"""
train_model.py - Model training script.

Loads the processed dataset from data/processed/, trains a scikit-learn
text classification pipeline (TF-IDF + classifier), evaluates performance,
and serialises the trained model to models/ using joblib.

Usage:
    python -m scripts.train_model
"""
