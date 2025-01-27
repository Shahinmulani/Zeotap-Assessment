
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Merge datasets
merged_data = transactions.merge(customers, on='CustomerID').merge(products, on='ProductID')

# Prepare customer data with aggregated metrics
customer_aggregates = merged_data.groupby('CustomerID').agg({
    'TotalValue': 'sum',  # Total revenue from the customer
    'Quantity': 'sum',    # Total quantity purchased
    'Category': lambda x: x.mode()[0]  # Most frequent product category purchased
}).reset_index()

# Encode categorical data (Category) into numeric format
customer_aggregates = pd.get_dummies(customer_aggregates, columns=['Category'], drop_first=True)

# Normalize numerical data (TotalValue and Quantity)
scaler = MinMaxScaler()
customer_aggregates[['TotalValue', 'Quantity']] = scaler.fit_transform(customer_aggregates[['TotalValue', 'Quantity']])

# Compute similarity matrix
features = customer_aggregates.drop('CustomerID', axis=1)  # Features excluding CustomerID
similarity_matrix = cosine_similarity(features)

# Find top 3 lookalikes for the first 20 customers (C0001 - C0020)
lookalike_results = {}
customer_ids = customer_aggregates['CustomerID'].values

for idx, customer_id in enumerate(customer_ids[:20]):
    # Get similarity scores for the current customer
    scores = similarity_matrix[idx]
    
    # Get the indices of the top 3 similar customers (excluding itself)
    top_indices = np.argsort(scores)[::-1][1:4]
    
    # Map CustomerID to top 3 similar customers with their similarity scores
    lookalike_results[customer_id] = [(customer_ids[i], scores[i]) for i in top_indices]

# Convert the lookalike results to a DataFrame for saving
lookalike_data = []
for customer, lookalikes in lookalike_results.items():
    lookalike_data.append({
        'CustomerID': customer,
        'Lookalike1': lookalikes[0][0],
        'Similarity1': lookalikes[0][1],
        'Lookalike2': lookalikes[1][0],
        'Similarity2': lookalikes[1][1],
        'Lookalike3': lookalikes[2][0],
        'Similarity3': lookalikes[2][1],
    })

lookalike_df = pd.DataFrame(lookalike_data)

# Save the lookalike results to a CSV file
lookalike_df.to_csv('Lookalike.csv', index=False)
