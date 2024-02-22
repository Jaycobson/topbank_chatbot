import pandas as pd
import numpy as np
import datetime

# Function to generate random bank transaction data
def generate_bank_transaction_data(num_transactions):
    data = []
    # Generate data starting from 50 days ago until today's date
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=50)
    # Initialize balance
    balance = 100000
    for i in range((end_date - start_date).days + 1):
        # Generate transaction date
        transaction_date = end_date - datetime.timedelta(days=50-i)
#         print(transaction_date)
        # Generate random reference (string)
        reference = np.random.choice(['REF123', 'REF456', 'REF789', 'REF987', 'REF654'])
        # Generate random debit amount
        debit = round(np.random.uniform(100, 10000), 2)
        # Generate random credit amount
        credit = round(np.random.uniform(100, 10000), 2)
        # Update balance based on debit and credit amounts
        balance = balance - debit + credit
        # Generate random remarks
        remarks = np.random.choice(['Salary', 'Utilities', 'Rent', 'Shopping', 'Transfer', 'Loan', 'Groceries','Education','Food'])
        data.append([transaction_date, reference, debit, credit, balance, remarks])

    return data

# Generate bank transaction data
num_transactions = 50  # Number of transactions to generate
bank_transaction_data = generate_bank_transaction_data(num_transactions)

# Create DataFrame from the generated data
columns = ['Date', 'Reference', 'Debit', 'Credit', 'Balance', 'Remarks']
df = pd.DataFrame(bank_transaction_data, columns=columns)

# Write DataFrame to CSV file
filename = 'bank_transactions.csv'
df.to_csv(filename, index=False)
print(f"CSV file '{filename}' created successfully.")
