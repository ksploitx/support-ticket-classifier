import sys
import os

# Ensure the app module can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.classifier import classify_ticket

test_cases = [
    "I cannot login to my account.",
    "Payment was deducted twice.",
    "How can I change my password?",
    "My order hasn't arrived.",
    "App crashes after opening.",
    "My account is locked",
    "The system is down",
    "I want a refund"
]

def main():
    print(f"{'Text':<40} | {'Category':<15} | {'Method':<17} | {'Confidence':<10}")
    print("-" * 90)

    for text in test_cases:
        res = classify_ticket(text)
        print(f"{text:<40} | {res['category']:<15} | {res['method']:<17} | {res['confidence']:.2f}")

if __name__ == '__main__':
    main()
