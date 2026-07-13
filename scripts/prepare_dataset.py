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
        'IT Support': 'Login Issue',
        'Product Support': 'Technical Issue',
        'Returns and Exchanges': 'Delivery',
        'Sales and Pre-Sales': 'Account',
        'Service Outages and Maintenance': 'Technical Issue',
        'Technical Support': 'Technical Issue'
    }
    df['category'] = df['queue'].map(queue_mapping)
    
    # Keep only the columns we need and drop any empty rows
    processed_df = df[['text', 'category']].dropna()
    
    # Save to processed folder
    print(f"Saving {len(processed_df)} processed records to {out_path}...")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    processed_df.to_csv(out_path, index=False)
    print("Done!")

if __name__ == "__main__":
    main()

