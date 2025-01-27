
# Data Science Assignment: eCommerce Transactions

This repository contains the deliverables for a comprehensive data science assignment focused on eCommerce transactions. The project involves exploratory data analysis (EDA), building a Lookalike Model, and performing Customer Segmentation using clustering techniques.

## Project Overview

### Objectives:

1. **Exploratory Data Analysis (EDA):**

   - Analyze datasets (`Customers.csv`, `Products.csv`, and `Transactions.csv`) to uncover patterns and trends.
   - Generate actionable business insights to improve decision-making.

2. **Lookalike Model:**

   - Develop a recommendation model that identifies top 3 similar customers based on their profile and transaction history.
   - Assign similarity scores for recommendations.

3. **Customer Segmentation (Clustering):**

   - Segment customers using clustering techniques to identify patterns in purchasing behavior.
   - Evaluate clusters using Davies-Bouldin Index and visualize the results.

## Repository Contents

### Files

1. **EDA Files:**

   - `EDA_Script.py`: Python script containing code for exploratory data analysis.
   - `EDA_Business_Insights.pdf`: PDF report summarizing business insights derived from the EDA.

2. **Lookalike Model Files:**

   - `Lookalike_Model.py`: Python script explaining the Lookalike Model development.
   - `Lookalike.csv`: Results containing the top 3 similar customers for CustomerID C0001 - C0020 with similarity scores.

3. **Clustering Files:**

   - `Clustering_Script.py`: Python script explaining the clustering process, metrics, and visualization.
   - `Clustering_Report.txt`: Text report summarizing clustering results, including the number of clusters, DB Index, and silhouette scores.
   - `Customer_Clusters.png`: Visualization of customer clusters using PCA.

### Datasets

The following datasets were provided for analysis:

- `Customers.csv`
- `Products.csv`
- `Transactions.csv`

## How to Use

### Running the Scripts

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Shahinmulani/Zeotap-Assessment
   ```
2. Navigate to the project folder:
   ```bash
   cd Zeotap-Assessment
   ```
3. Run the Python scripts in the following order:
   - `EDA_Script.py`: Perform exploratory data analysis and derive insights.
   - `Lookalike_Model.py`: Generate Lookalike recommendations.
   - `Clustering_Script.py`: Perform customer segmentation and visualize clusters.

### Viewing Reports

- Open `EDA_Business_Insights.pdf` for EDA insights.
- Open `Clustering_Report.txt` for clustering metrics and results.

## Key Results

1. **EDA Insights:**

   - South America generates the highest revenue among regions.
   - Clothing and Books dominate sales, with significant contributions from Electronics.
   - Seasonal transaction trends were observed.

2. **Lookalike Model:**

   - Top 3 similar customers identified for each of the first 20 customers.
   - Similarity scores calculated using normalized transaction data.

3. **Clustering Results:**

   - Optimal number of clusters: `<number>` (based on DB Index).
   - Best DB Index: `<value>`
   - Customer clusters visualized in `Customer_Clusters.png`.

## Tools and Libraries

- Python 3
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## Contact

For any questions or feedback, please reach out to:

- **Name**: Shahin Mulani
- **Email**: shahinmulani796@gmail.com

---

Thank you
