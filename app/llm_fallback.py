"""
llm_fallback.py - LLM-based fallback classifier.

When both rule-based and ML-based classifiers fail to produce a confident
prediction, this module sends the ticket text to an LLM (e.g. OpenAI GPT)
for zero-shot classification. Handles prompt construction, API calls,
response parsing, and error handling / retries.
"""
