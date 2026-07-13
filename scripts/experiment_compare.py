import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score, f1_score
import random

def main():
    print("Loading data...")
    data_path = "data/processed/labeled_tickets.csv"
    df = pd.read_csv(data_path)
    
    X = df['text']
    y = df['category']

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

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

    models = {
        "LR (balanced)": LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
        "LR (none)": LogisticRegression(class_weight=None, max_iter=1000, random_state=42),
        "LinearSVC (balanced)": LinearSVC(class_weight='balanced', max_iter=10000, random_state=42),
        "LinearSVC (none)": LinearSVC(class_weight=None, max_iter=10000, random_state=42)
    }

    results = []
    best_variant = None
    best_macro_f1 = -1
    best_preds = None

    print("\nTraining and evaluating models...\n")
    for name, model in models.items():
        model.fit(X_train_vec, y_train)
        y_pred = model.predict(X_test_vec)
        
        acc = accuracy_score(y_test, y_pred)
        macro_f1 = f1_score(y_test, y_pred, average='macro')
        
        # Get per-class F1 for Account and Technical Issue
        report = classification_report(y_test, y_pred, output_dict=True)
        f1_account = report['Account']['f1-score']
        f1_tech = report['Technical Issue']['f1-score']
        
        results.append({
            "Variant": name,
            "Macro F1": f"{macro_f1:.4f}",
            "Accuracy": f"{acc:.4f}",
            "Account F1": f"{f1_account:.4f}",
            "Tech Issue F1": f"{f1_tech:.4f}"
        })
        
        if macro_f1 > best_macro_f1:
            best_macro_f1 = macro_f1
            best_variant = name
            best_preds = y_pred

    print("--- Comparison Table ---")
    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))
    
    print(f"\nBest variant based on Macro F1: {best_variant}")
    print("\n--- 10 Random Misclassified Examples (Account <-> Technical Issue) ---")
    
    # Identify confusions between Account and Technical Issue
    confused_indices = []
    y_test_list = y_test.tolist()
    y_pred_list = best_preds.tolist()
    X_test_list = X_test.tolist()
    
    for i in range(len(y_test_list)):
        true_label = y_test_list[i]
        pred_label = y_pred_list[i]
        
        if true_label != pred_label:
            if (true_label == 'Account' and pred_label == 'Technical Issue') or \
               (true_label == 'Technical Issue' and pred_label == 'Account'):
                confused_indices.append(i)
                
    # Sample up to 10
    sample_size = min(10, len(confused_indices))
    sampled_indices = random.sample(confused_indices, sample_size)
    
    for idx, i in enumerate(sampled_indices):
        true_label = y_test_list[i]
        pred_label = y_pred_list[i]
        text = X_test_list[i]
        print(f"\nExample {idx+1}:")
        print(f"True: {true_label} | Predicted: {pred_label}")
        print(f"Text: {text}")

if __name__ == "__main__":
    main()
