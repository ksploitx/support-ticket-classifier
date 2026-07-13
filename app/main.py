"""
main.py - FastAPI application entrypoint.

Defines the FastAPI app instance, registers API routes for ticket
classification, and configures startup events (e.g. loading the trained
model into memory). Run with:

    uvicorn app.main:app --reload
"""
