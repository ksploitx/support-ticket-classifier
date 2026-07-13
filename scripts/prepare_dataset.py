# Script to process raw data into training format

import pandas as pd
import os

def main():
    print("Loading raw dataset...")
    raw_path = "data/raw/Ticket Dataset Multi-Lang.csv"
    out_path = "data/processed/labeled_tickets.csv"
    
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found.")
        return

    df = pd.read_csv(raw_path)
    
    # Create the 'text' column by combining subject and body
    print("Processing features...")
    df['text'] = df['subject'].fillna('') + " " + df['body'].fillna('')
    
    # Rename 'queue' to 'category' for the model
    print("Mapping labels...")
    queue_mapping = {
        'Billing and Payments': 'Payment',
        'Customer Service': 'Account',
        'General Inquiry': 'Others',
        'Human Resources': 'Others',
        'Product Support': 'Technical Issue',
        'Returns and Exchanges': 'Delivery',
        'Sales and Pre-Sales': 'Others',
        'Service Outages and Maintenance': 'Technical Issue'
    }
    
    def map_category(row):
        q = row['queue']
        text = str(row['text']).lower()
        if q in ['IT Support', 'Technical Support']:
            login_keywords = ['login', 'log in', 'password', 'otp', 'sign in', 'signin', 'authenticate', 'authentication', 'locked out', 'access denied', "can't access my account", 'reset my password']
            if any(kw in text for kw in login_keywords):
                return 'Login Issue'
            return 'Technical Issue'
        return queue_mapping.get(q, 'Others')
        
    df['category'] = df.apply(map_category, axis=1)
    
    # Keep only the columns we need and drop any empty rows
    processed_df = df[['text', 'category']].dropna()
    
    # Save to processed folder
    print(f"Saving {len(processed_df)} processed records to {out_path}...")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    processed_df.to_csv(out_path, index=False)
    print("Done!")

if __name__ == "__main__":
    main()

