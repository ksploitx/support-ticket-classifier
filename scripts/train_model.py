import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
import joblib

def main():
    print("Loading data...")
    # 1. Load the CSV
    data_path = "data/processed/labeled_tickets.csv"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Please ensure the processed data exists.")
        return
        
    df = pd.read_csv(data_path)
    
    # Assuming 'text' is the feature column and 'category' is the label
    # (Adjust column names if your CSV uses different headers)
    X = df['text']
    y = df['category']

    # 2. Train/test split, 80/20, stratified by category
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # 3. TfidfVectorizer
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(
        strip_accents='unicode',
        ngram_range=(1, 2),
        min_df=2,
        max_features=5000,
        stop_words='english'
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 4. LogisticRegression
    print("Training model...")
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    
    # 5. Fit, print classification_report and confusion matrix
    model.fit(X_train_vec, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test_vec)
    
    print("\n--- Classification Report ---")
    print(classification_report(y_test, y_pred))
    
    print("--- Confusion Matrix ---")
    print(confusion_matrix(y_test, y_pred))
    
    # Final metrics
    acc = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average='macro')
    print(f"\nFinal Test Accuracy: {acc:.4f}")
    print(f"Final Macro F1 Score: {macro_f1:.4f}")

    # 6. Save vectorizer and model using joblib
    print("\nSaving artifacts...")
    os.makedirs("models", exist_ok=True)
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    joblib.dump(model, "models/model.pkl")

    # 7. Save the sorted list of class labels
    labels = sorted(model.classes_.tolist())
    with open("models/labels.json", "w") as f:
        json.dump(labels, f, indent=4)
        
    print("Training complete! Model, vectorizer, and labels saved to models/ directory.")

if __name__ == "__main__":
    main()
