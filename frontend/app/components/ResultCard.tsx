"use client";

import React from "react";

/* ── Types ── */
interface ClassifyResult {
  category: string;
  confidence: number | null;
  method: string;
}

interface ResultCardProps {
  result: ClassifyResult;
}

/* ── Method label mapping ── */
const METHOD_LABELS: Record<string, string> = {
  rule: "Rule-based match",
  ml: "ML prediction",
  ml_low_confidence: "ML (low confidence) → Others",
  llm_fallback: "AI fallback used",
};

/* ── Category pill colors ── */
const CATEGORY_COLORS: Record<string, { bg: string; text: string }> = {
  "Login Issue": { bg: "bg-cat-login-bg", text: "text-cat-login-text" },
  Payment: { bg: "bg-cat-payment-bg", text: "text-cat-payment-text" },
  Account: { bg: "bg-cat-account-bg", text: "text-cat-account-text" },
  Delivery: { bg: "bg-cat-delivery-bg", text: "text-cat-delivery-text" },
  "Technical Issue": {
    bg: "bg-cat-technical-bg",
    text: "text-cat-technical-text",
  },
};

const DEFAULT_COLORS = { bg: "bg-cat-others-bg", text: "text-cat-others-text" };

export default function ResultCard({ result }: ResultCardProps) {
  const colors = CATEGORY_COLORS[result.category] || DEFAULT_COLORS;
  const confidencePercent =
    result.confidence != null ? Math.round(result.confidence * 100) : null;
  const methodLabel = METHOD_LABELS[result.method] || result.method;

  return (
    <div className="bg-surface-container-lowest border border-elevation-border rounded-lg p-6 shadow-elevation-1">
      <h3 className="text-[12px] leading-[14px] font-semibold text-outline uppercase tracking-wide mb-4">
        Classification Result
      </h3>

      {/* ── Category pill ── */}
      <div className="flex items-center gap-3">
        <span
          className={`inline-block px-3 py-1 rounded-full text-[12px] leading-[14px] font-semibold ${colors.bg} ${colors.text}`}
        >
          {result.category}
        </span>
      </div>

      {/* ── Confidence bar ── */}
      {confidencePercent != null && (
        <div className="mt-4">
          <div className="flex items-center gap-3">
            <div className="flex-1 h-2 bg-surface-container-high rounded-full overflow-hidden">
              <div
                className="h-full bg-primary rounded-full transition-all duration-500 ease-out"
                style={{ width: `${confidencePercent}%` }}
              />
            </div>
            <span className="text-[14px] leading-[16px] font-medium text-on-surface min-w-[3rem] text-right">
              {confidencePercent}%
            </span>
          </div>
        </div>
      )}

      {/* ── Method tag ── */}
      <div className="mt-3">
        <span className="text-[12px] leading-[14px] font-semibold text-outline">
          {methodLabel}
        </span>
      </div>
    </div>
  );
}
