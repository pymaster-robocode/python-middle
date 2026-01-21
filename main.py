import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('choco.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.strftime('%B')
df['Amount'] = df['Amount'].str.replace('$', '').str.replace(',', '').astype(float)

fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle('Choco sales analytics')

monthly = df.groupby('Month')['Amount'].sum()
axes[0, 0].bar(monthly.index, monthly.values)
axes[0, 0].set_title('Monthly Sales')
axes[0, 0].set_ylabel('Summ ($)')

daily = df.sort_values('Date')
axes[0, 1].plot(daily['Date'], daily['Amount'], marker='o', markersize=8, markeredgecolor='black')
axes[0, 1].set_title('Sales trend')
axes[0, 1].set_ylabel('Summ ($)')

country = df.groupby('Country')['Amount'].sum()
axes[1, 0].bar(country.index, country.values)
axes[1, 0].set_title('Sales by countries')
axes[1, 0].set_ylabel('Summ ($)')

country_avg = df.groupby('Country')['Amount'].mean()
axes[1, 1].barh(country_avg.index, country_avg.values)
axes[1, 1].set_title('Avg check by Countries')
axes[1, 1].set_xlabel('Avg summ ($)')

df['Price_per_Box'] = df['Amount'] / df['Boxes Shipped']
axes[2, 0].scatter(df['Boxes Shipped'], df['Amount'], alpha=0.1,
                   c=df['Price_per_Box'])
axes[2, 0].set_title('Correlation: Box vs Income')
axes[2, 0].set_xlabel('Box count')
axes[2, 0].set_ylabel('Income ($)')

seller_stats = df.groupby('Sales Person').agg({
    'Amount': 'sum',
    'Boxes Shipped': 'sum'
}).reset_index()
seller_stats['Efficiency'] = seller_stats['Amount'] / seller_stats['Boxes Shipped']
seller_stats = seller_stats.sort_values('Efficiency').head(10)
axes[2, 1].barh(seller_stats['Sales Person'], seller_stats['Efficiency'])
axes[2, 1].set_title('Top 10 sellers')
axes[2, 1].set_xlabel('Efficiency ($ per box)')

plt.tight_layout()
plt.show()


df["Date_ordinal"] = df["Date"].map(pd.Timestamp.toordinal)
numeric_df = df.select_dtypes(include=["number"])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()