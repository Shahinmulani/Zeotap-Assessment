
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.metrics import davies_bouldin_score, silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Merge datasets
merged_data = transactions.merge(customers, on='CustomerID').merge(products, on='ProductID')

# Aggregating data for clustering
clustering_data = merged_data.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum'
}).reset_index()

# Normalize data
scaler = MinMaxScaler()
clustering_data[['TotalValue', 'Quantity']] = scaler.fit_transform(clustering_data[['TotalValue', 'Quantity']])

# Apply KMeans clustering
db_scores = []
silhouette_scores = []
clusters_range = range(2, 11)
models = {}

for k in clusters_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    clustering_data['Cluster'] = kmeans.fit_predict(clustering_data[['TotalValue', 'Quantity']])
    db_index = davies_bouldin_score(clustering_data[['TotalValue', 'Quantity']], clustering_data['Cluster'])
    silhouette = silhouette_score(clustering_data[['TotalValue', 'Quantity']], clustering_data['Cluster'])
    db_scores.append(db_index)
    silhouette_scores.append(silhouette)
    models[k] = kmeans

# Determine optimal number of clusters
optimal_k = clusters_range[db_scores.index(min(db_scores))]
best_kmeans = models[optimal_k]
clustering_data['Cluster'] = best_kmeans.predict(clustering_data[['TotalValue', 'Quantity']])

# Visualize Clusters using PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(clustering_data[['TotalValue', 'Quantity']])
clustering_data['PCA1'] = reduced_data[:, 0]
clustering_data['PCA2'] = reduced_data[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=clustering_data, palette='viridis')
plt.title(f'Customer Clusters (Optimal K={optimal_k})')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend(title='Cluster')
plt.tight_layout()
plt.savefig('Customer_Clusters.png')
plt.show()
