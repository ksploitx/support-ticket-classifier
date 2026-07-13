"use client";

import React from "react";

/* ── Example chips data ── */
const EXAMPLES = [
  { label: "Login Issue", text: "I cannot login to my account." },
  { label: "Payment Error", text: "Payment was deducted twice." },
  { label: "Shipping Status", text: "My order hasn't arrived." },
] as const;

const MAX_CHARS = 500;

interface TicketFormProps {
  ticketText: string;
  setTicketText: (text: string) => void;
  useFallback: boolean;
  setUseFallback: (value: boolean) => void;
  onClassify: () => void;
  loading: boolean;
  error: string | null;
}

export default function TicketForm({
  ticketText,
  setTicketText,
  useFallback,
  setUseFallback,
  onClassify,
  loading,
  error,
}: TicketFormProps) {
  const isEmpty = ticketText.trim().length === 0;

  return (
    <div className="bg-surface-container-lowest border border-elevation-border rounded-lg p-6 shadow-elevation-1">
      {/* ── Header ── */}
      <h2 className="text-[20px] leading-[28px] font-semibold text-on-surface">
        TicketSense
      </h2>
      <p className="text-[14px] leading-[20px] text-on-surface-variant mt-1">
        Classify support tickets instantly.
      </p>

      {/* ── Example chips ── */}
      <div className="mt-5">
        <span className="text-[12px] leading-[14px] font-semibold text-outline uppercase tracking-wide">
          Try an Example
        </span>
        <div className="flex flex-wrap gap-2 mt-2.5">
          {EXAMPLES.map((example) => (
            <button
              key={example.label}
              type="button"
              onClick={() => setTicketText(example.text)}
              className="px-3 py-1.5 text-[14px] leading-[16px] font-medium text-on-surface-variant
                         border border-outline-variant rounded-md
                         hover:bg-surface-container-low hover:border-outline
                         transition-colors cursor-pointer"
            >
              {example.label}
            </button>
          ))}
        </div>
      </div>

      {/* ── Textarea ── */}
      <div className="relative mt-4">
        <textarea
          id="ticket-input"
          value={ticketText}
          onChange={(e) => {
            if (e.target.value.length <= MAX_CHARS) {
              setTicketText(e.target.value);
            }
          }}
          placeholder='Paste or type a support ticket, e.g. "I cannot login to my account."'
          maxLength={MAX_CHARS}
          rows={5}
          className="w-full bg-surface-container-lowest border border-input-border rounded-md
                     px-4 pt-3 pb-8 text-[16px] leading-[24px] text-on-surface
                     placeholder:text-outline resize-none
                     focus:outline-none focus:ring-2 focus:ring-input-focus-ring
                     transition-shadow"
        />
        <span className="absolute bottom-2.5 right-3 text-[12px] leading-[14px] font-semibold text-outline">
          {ticketText.length}/{MAX_CHARS}
        </span>
      </div>

      {/* ── AI fallback toggle ── */}
      <label
        htmlFor="fallback-toggle"
        className="flex items-center gap-3 mt-4 cursor-pointer select-none"
      >
        <button
          id="fallback-toggle"
          type="button"
          role="switch"
          aria-checked={useFallback}
          onClick={() => setUseFallback(!useFallback)}
          className={`relative inline-flex h-6 w-11 shrink-0 rounded-full border-2 border-transparent
                      transition-colors duration-200 ease-in-out cursor-pointer
                      focus:outline-none focus:ring-2 focus:ring-input-focus-ring
                      ${useFallback ? "bg-primary" : "bg-outline-variant"}`}
        >
          <span
            className={`pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow-sm
                        transform transition-transform duration-200 ease-in-out
                        ${useFallback ? "translate-x-5" : "translate-x-0"}`}
          />
        </button>
        <span className="text-[14px] leading-[20px] text-on-surface-variant">
          Use AI fallback for uncertain tickets
        </span>
      </label>

      {/* ── Classify button ── */}
      <button
        id="classify-button"
        type="button"
        disabled={isEmpty || loading}
        onClick={onClassify}
        className="mt-5 w-full py-2.5 px-4 rounded-md text-[14px] leading-[16px] font-medium
                   bg-primary text-on-primary
                   hover:bg-primary-container
                   disabled:opacity-50 disabled:cursor-not-allowed
                   transition-colors cursor-pointer
                   flex items-center justify-center gap-2"
      >
        {loading && (
          <svg
            className="animate-spin h-4 w-4 text-on-primary"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
        )}
        {loading ? "Classifying…" : "Classify Ticket"}
      </button>

      {/* ── Inline error ── */}
      {error && (
        <div className="mt-3 px-3 py-2 rounded-md bg-error-container text-[14px] leading-[20px] text-on-surface">
          {error}
        </div>
      )}
    </div>
  );
}
