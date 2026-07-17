import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import StrMethodFormatter


plt.style.use('seaborn-v0_8')
# Read data
transactions_data = pd.read_csv('data/transactions_data.csv')
transactions_data['amount'] = transactions_data['amount'].str.replace('$', '', regex=False).astype(float)

# Analyse data
print(transactions_data.dtypes)
print('Number of Missing Values', transactions_data['amount'].isna().sum())
print('Number of Negative Transactions', transactions_data['amount'].lt(0).sum())
print(transactions_data['amount'].min())
print(transactions_data['amount'].max())
## Transaction amount
amount = transactions_data['amount']
median = amount.quantile(0.5)
p95 = amount.quantile(0.95)
p99 = amount.quantile(0.99)
print(transactions_data['amount'].quantile([0.5, 0.75, 0.9, 0.95, 0.99]))

"""
The transaction amount distribution is highly right-skewed. The median transaction amount
is only $28.99, while 99% of transactions are below $315.95. A small number of high-value 
transactions extend to several thousand dollars and create a long upper tail in the distribution.
A logarithmic scale is useful for visualizing both common and rare transactions 
within the same chart.
"""

# Create SubPlots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(16, 12))
# Row distribution
ax1.hist(amount, bins=50, edgecolor='black', label='Raw Distribution')
# Log-scaled distribution
ax2.hist(amount, bins=50, edgecolor='black', label='Log-scaled distribution', log=True)

# Visualize Quantiles
ax1.axvline(median, color='red', linestyle='--', label='median')
ax1.axvline(p95, color='yellow', linestyle='--', label='95th Percentile')
ax1.axvline(p99, color='green', linestyle='--', label='99th Percentile')

ax2.axvline(median, color='red', linestyle='--', label='median')
ax2.axvline(p95, color='yellow', linestyle='--', label='95th Percentile')
ax2.axvline(p99, color='green', linestyle='--', label='99th Percentile')

# Visualization Formatting
fig.suptitle('Transaction Amount Distribution', fontsize=20)
ax1.grid(alpha=0.3)
ax2.grid(alpha=0.3)

ax1.legend()
ax1.set_title('Transactions Amount (USD $)')
# ax1.set_xlabel('Amount (USD)')
ax1.set_ylabel('')
ax2.legend()
ax2.set_title('Log-Scaled Distribution')
ax2.set_xlabel('Amount (USD)')
ax2.set_ylabel('')
ax2.xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
fig.supylabel('Number of Transactions')
plt.tight_layout()
plt.savefig('images/transactions_hist.png')
plt.show()

"""
Insights from Visualization
The transaction amount distribution is heavily right-skewed.
The median transaction amount is 28.99, indicating that a typical transaction is relatively small.
75% of transactions are below $63.71.
99% of transactions are below $315.95.
A relatively small number of extremely large transactions extend to approximately $7000 
        and create a long right tail.
Because of this imbalance, a logarithmic scale provides a clearer view of both common 
        and rare transactions.
Negative transaction amounts are present and may represent refunds, reversals, or adjustments.
    """
