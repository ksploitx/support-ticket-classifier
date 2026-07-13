"use client";

import React, { useState } from "react";
import TicketForm from "./components/TicketForm";
import ResultCard from "./components/ResultCard";

/* ── Types ── */
interface ClassifyResult {
  category: string;
  confidence: number | null;
  method: string;
}

const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function Home() {
  const [ticketText, setTicketText] = useState("");
  const [useFallback, setUseFallback] = useState(false);
  const [result, setResult] = useState<ClassifyResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleClassify() {
    setLoading(true);
    setError(null);

    const endpoint = useFallback
      ? `${API_URL}/classify?fallback=llm`
      : `${API_URL}/classify`;

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: ticketText }),
      });

      if (!res.ok) {
        const detail = await res.text();
        throw new Error(`Server error (${res.status}): ${detail}`);
      }

      const data: ClassifyResult = await res.json();
      setResult(data);
    } catch (err) {
      setResult(null);
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong. Please try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col min-h-screen">
      {/* ── Header bar ── */}
      <header className="flex items-center justify-between px-6 py-3 border-b border-elevation-border bg-surface-container-lowest">
        <h1 className="text-[20px] leading-[28px] font-semibold text-on-surface">
          TicketSense
        </h1>
        <div className="flex items-center gap-3">
          {/* Help icon */}
          <button
            type="button"
            aria-label="Help"
            className="p-1.5 rounded-md text-on-surface-variant hover:bg-surface-container-low transition-colors cursor-pointer"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="12" cy="12" r="10" />
              <path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3" />
              <line x1="12" y1="17" x2="12.01" y2="17" />
            </svg>
          </button>
          {/* Settings icon */}
          <button
            type="button"
            aria-label="Settings"
            className="p-1.5 rounded-md text-on-surface-variant hover:bg-surface-container-low transition-colors cursor-pointer"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="12" cy="12" r="3" />
              <path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z" />
            </svg>
          </button>
        </div>
      </header>

      {/* ── Main content ── */}
      <main className="flex-1 flex items-start justify-center px-4 py-12">
        <div className="w-full max-w-lg flex flex-col gap-5">
          <TicketForm
            ticketText={ticketText}
            setTicketText={setTicketText}
            useFallback={useFallback}
            setUseFallback={setUseFallback}
            onClassify={handleClassify}
            loading={loading}
            error={error}
          />

          {result && <ResultCard result={result} />}
        </div>
      </main>
    </div>
  );
}
