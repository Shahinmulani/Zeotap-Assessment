
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Combine the datasets
merged_data = transactions.merge(customers, on='CustomerID').merge(products, on='ProductID')

# Revenue by Region
revenue_by_region = merged_data.groupby('Region')['TotalValue'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=revenue_by_region.index, y=revenue_by_region.values, palette="viridis")
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_by_region.png')

# Top 10 Products by Revenue
top_products = merged_data.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="mako")
plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Revenue (USD)')
plt.ylabel('Product Name')
plt.tight_layout()
plt.savefig('top_products_by_revenue.png')

# Transactions Over Time
merged_data['TransactionDate'] = pd.to_datetime(merged_data['TransactionDate'])
transactions_over_time = merged_data.set_index('TransactionDate').resample('M')['TransactionID'].count()
plt.figure(figsize=(10, 6))
transactions_over_time.plot(kind='line', marker='o', color='teal')
plt.title('Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.savefig('transactions_over_time.png')

# Revenue by Product Category
revenue_by_category = merged_data.groupby('Category')['TotalValue'].sum()
plt.figure(figsize=(8, 5))
sns.barplot(x=revenue_by_category.values, y=revenue_by_category.index, palette="cubehelix")
plt.title('Revenue by Product Category')
plt.xlabel('Total Revenue (USD)')
plt.ylabel('Product Category')
plt.tight_layout()
plt.savefig('revenue_by_category.png')

# Quantity Distribution
plt.figure(figsize=(8, 5))
sns.histplot(merged_data['Quantity'], kde=True, bins=10, color='coral')
plt.title('Distribution of Product Quantities Purchased')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('quantity_distribution.png')
