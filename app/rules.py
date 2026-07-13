# Rule-based ticket classification using simple keyword matching

import re
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Category → keyword mapping
#
# Each keyword is matched using word-boundary anchors (\b) so that
# "pay" won't accidentally match "display" or "repay".
# ---------------------------------------------------------------------------

CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "Billing and Payments": [
        "invoice", "billing", "payment", "refund", "charge", "charged",
        "credit card", "debit card", "receipt", "subscription",
        "overcharged", "transaction", "pricing", "price",
        "pay", "paid", "outstanding balance", "due date",
    ],
    "Technical Support": [
        "error", "bug", "crash", "not working", "broken", "glitch",
        "exception", "traceback", "stack trace", "slow", "latency",
        "timeout", "freeze", "unresponsive", "compatibility",
        "driver", "firmware", "update failed",
    ],
    "Account and Access": [
        "password", "login", "sign in", "locked out", "reset",
        "two factor", "2fa", "mfa", "credentials", "username",
        "account", "permission", "access denied", "sso",
        "authentication", "authorization", "vpn",
    ],
    "Returns and Exchanges": [
        "return", "exchange", "refund", "damaged", "defective",
        "wrong item", "replacement", "rma", "warranty",
        "shipping back", "return label", "send back",
    ],
    "Outage and Maintenance": [
        "outage", "downtime", "maintenance", "offline", "unavailable",
        "system down", "service disruption", "status page",
        "scheduled maintenance", "degraded", "incident",
    ],
    "Sales and Pre-Sales": [
        "demo", "trial", "purchase", "buying", "quote",
        "discount", "coupon", "promo", "sales team",
        "interested in", "proposal", "upgrade plan",
        "enterprise plan", "bulk order",
    ],
}


def _compile_patterns(
    keywords: Dict[str, List[str]],
) -> Dict[str, List[re.Pattern]]:
    """Pre-compile word-boundary regex patterns for every keyword."""
    compiled: Dict[str, List[re.Pattern]] = {}
    for category, words in keywords.items():
        compiled[category] = [
            re.compile(r"\b" + re.escape(w) + r"\b", re.IGNORECASE)
            for w in words
        ]
    return compiled


_COMPILED = _compile_patterns(CATEGORY_KEYWORDS)


def classify_by_rules(text: str) -> Optional[str]:
    """
    Score each category by the number of keyword matches found in *text*.

    Returns the winning category name if:
      - it has at least 1 match, AND
      - it has a strict lead over the runner-up (no tie).

    Returns None when the rules are inconclusive so the ML model
    can take over.
    """
    text = text.lower()

    # Score every category
    scores: Dict[str, int] = {}
    for category, patterns in _COMPILED.items():
        score = sum(1 for p in patterns if p.search(text))
        if score > 0:
            scores[category] = score

    if not scores:
        return None

    # Sort descending by score
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)

    top_category, top_score = ranked[0]

    # If there's a runner-up with the same score → tie → defer to ML
    if len(ranked) > 1 and ranked[1][1] == top_score:
        return None

    return top_category


# ---------------------------------------------------------------------------
# Inline test cases (expected input → output)
# ---------------------------------------------------------------------------
#
# >>> classify_by_rules("I was charged twice on my credit card for the subscription")
# 'Billing and Payments'
#
# >>> classify_by_rules("The display on my monitor is flickering after the firmware update")
# 'Technical Support'          # "display" does NOT trigger "pay" match
#
# >>> classify_by_rules("I can't login, my account is locked out after too many attempts")
# 'Account and Access'
#
# >>> classify_by_rules("I received a damaged item and need a replacement")
# 'Returns and Exchanges'
#
# >>> classify_by_rules("Your service is down and the status page shows a major outage")
# 'Outage and Maintenance'
#
# >>> classify_by_rules("Hello, I just have a random question about the weather")
# None                         # No strong match → defer to ML
#
# >>> classify_by_rules("I need my password and also a refund")
# None                         # Tie between Account/Access and Billing (score 1 each) → defer to ML
