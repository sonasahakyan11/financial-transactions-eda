# Financial Transactions EDA

## Project Overview
This project performs Exploratory Data Analysis (EDA) on a financial transactions dataset using Python, Pandas, and Matplotlib.
The analysis focuses on:

- Transaction amount distributions
- Outlier detection
- Merchant location performance
- Business insights derived from transaction data

## Dataset

The dataset used in this project is available on Kaggle:

[https://www.kaggle.com/datasets/...](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)

Download the CSV file and place it in the `data/` folder before running the project.

## Transaction Amount Distribution

### Business Question
How are transaction amounts distributed across all transactions?

### Visualization
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/ef332fd2-5898-4cc1-9044-c0857093bca0" />

### Insights

- Median transaction amount: $28.99
- 99% of transactions are below $315.95
- Distribution is heavily right-skewed

## Top Merchant Locations by Total Sales

### Business Question
Which merchant locations generate the highest total sales volume?

### Visualization
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/93b6c5b4-4852-411f-b549-554239dad2e4" />

### Insights

- ONLINE generated the highest total sales volume.
- Houston generated the highest total sales among physical locations.
- Sales are concentrated in ONLINE transactions.

