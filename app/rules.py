"""
rules.py - Rule-based ticket classification heuristics.

Implements keyword-matching and regex-based rules for fast, deterministic
ticket classification. Used as the first pass before the ML model to handle
common, well-understood ticket patterns (e.g. password resets, billing
inquiries) without incurring model inference overhead.
"""
