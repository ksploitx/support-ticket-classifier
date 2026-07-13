"""
classifier.py - ML-based ticket classification logic.

Loads the trained scikit-learn model (via joblib) and exposes a prediction
interface. This module handles text preprocessing, feature extraction, and
model inference for incoming support tickets. Falls back to rule-based or
LLM classification when confidence is below a threshold.
"""
