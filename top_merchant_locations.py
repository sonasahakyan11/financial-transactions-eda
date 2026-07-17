import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

plt.style.use('seaborn-v0_8')
plt.figure(figsize=(12, 6))

# Read Data
data = pd.read_csv('data/transactions_data.csv')

# Data Analysis
print(data.head())
print(data.info())
print(data.describe())

data['amount'] = data['amount'].str.replace('$', '', regex=False).astype(float)
print('Missing Merchant City Values:', data['merchant_city'].isna().sum())

# Get Transactions Amount of Merchant Cities
top_10_merchant_locations = (
    data.groupby('merchant_city', as_index=False)
        .agg(total_sales = ('amount', 'sum'))
        .sort_values(by='total_sales', ascending=False).head(10)
)

print(top_10_merchant_locations.head(10))

# Visualization
## Get columns
cities = top_10_merchant_locations['merchant_city']
total_sales = top_10_merchant_locations['total_sales']
cities = cities.iloc[::-1]
total_sales = total_sales.iloc[::-1]
plt.barh(cities, total_sales)

plt.title('Top 10 Merchant Locations by Total Sales')
plt.gca().xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
plt.grid(axis='x', alpha=0.3)
plt.xlabel('Total Sales')
plt.ylabel('Merchant Locations')
plt.tight_layout()
plt.savefig('images/top_locations_by_sale.png')
plt.show()

"""
Insights

ONLINE generated the highest total sales volume, significantly exceeding any individual physical merchant location.
Sales are highly concentrated in ONLINE transactions and a small number of physical locations.
Among physical locations, Houston generated the highest total sales.
The concentration of sales within ONLINE suggests that e-commerce activity 
    contributes substantially to overall transaction volume.
Because ONLINE sales are substantially larger than sales from physical locations, 
    additional analysis excluding ONLINE may provide clearer insight into geographic transaction patterns.
    """