# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_excel("C:\Users\Admin\Downloads\sales.csv")

# df.head()

# # Check basic info
# df.info()

# # Check summary statistics
# df.describe()

# # Check missing values
# df.isnull().sum()

# # Example: Total sales by region
# region_sales = df.groupby("Region")["Sales"].sum()
# print(region_sales)

# # Example: Total sales by product
# product_sales = df.groupby("Product")["Sales"].sum()
# print(product_sales)


# # Plot total sales by region
# region_sales.plot(kind='bar', color='skyblue', title='Total Sales by Region')
# plt.xlabel('Region')
# plt.ylabel('Sales')
# plt.show()

# # Plot total sales by product
# sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
# plt.title("Total Sales by Product")
# plt.xticks(rotation=45)
# plt.show()




import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2025-01-01', periods=12, freq='M'),
    'Region': ['North', 'South', 'East', 'West'] * 3,
    'Product': ['Laptop', 'Tablet', 'Phone', 'Laptop'] * 3,
    'Units_Sold': [120, 85, 150, 110, 130, 90, 170, 100, 140, 95, 180, 105],
    'Unit_Price': [800, 300, 500, 850, 820, 320, 520, 870, 810, 310, 510, 860]
}

sales_df = pd.DataFrame(data)
sales_df['Total_Sales'] = sales_df['Units_Sold'] * sales_df['Unit_Price']

sales_df.to_csv('sales_data.csv', index=False)
print(" Sample CSV file 'sales_data.csv' created successfully!")
df = pd.read_csv('sales_data.csv')#ELLI ATTACH MADINI NODU
print("\n Preview of data:")
print(df.head())


print("\n Basic Info:")
print(df.info())

print("\n Summary Statistics:")
print(df.describe())

region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()
print("\n Total Sales by Region:")
print(region_sales)

product_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()
print("\n Total Sales by Product:")
print(product_sales)


plt.figure(figsize=(8,5))
plt.bar(region_sales['Region'], region_sales['Total_Sales'])
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

plt.figure(figsize=(6,6))
plt.pie(product_sales['Total_Sales'], labels=product_sales['Product'], autopct='%1.1f%%')
plt.title('Sales Share by Product')
plt.show()

