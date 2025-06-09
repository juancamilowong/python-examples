import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Load dataset  
df = pd.read_csv('data/sales.csv', encoding="latin1")
df = df.drop('Row ID', axis=1)

# Explore the dataset
print(df.info())


# Clean the dataset0
df.fillna(0, inplace=True)  # Fill NaN values with 0
# Ensure 'Order Date' is in datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Aggregate sales by region
sales_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(sales_by_region.head())

# Visualize sales by region
sales_by_region.plot(kind='bar', title='Sales by Region', color='skyblue')
plt.ylabel('Total Profit')
plt.show()

best_seller_product = df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False)
print(best_seller_product.head())

more_income_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(more_income_category.head())

df["period"] = df["Order Date"].dt.to_period("M")

sells_by_dayte = df.groupby('period')['Profit'].sum().sort_values(ascending=False).reset_index()
print(sells_by_dayte.head())

# Visualize sales by date
sells_by_dayte.plot(kind='bar', title='Sales by Date', color='skyblue')
plt.ylabel('Total Profit')
plt.show()

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))
monthly_sales = monthly_sales.sort_values('Date')

monthly_sales['TimeIndex'] = np.arange(len(monthly_sales)) 
X = monthly_sales[['TimeIndex']]  # input (meses)
y = monthly_sales['Sales']        # target (ventas)

# Crear y entrenar modelo
model = LinearRegression()
model.fit(X, y)
monthly_sales['Predicted_Sales'] = model.predict(X)

# Predecir para 12 meses futuros
future_index = np.arange(len(monthly_sales), len(monthly_sales) + 12).reshape(-1, 1)
future_preds = model.predict(future_index)

# Crear DataFrame con fechas futuras
future_dates = pd.date_range(start=monthly_sales['Date'].iloc[-1] + pd.DateOffset(months=1), periods=12, freq='MS')
future_df = pd.DataFrame({
    'Date': future_dates,
    'TimeIndex': future_index.flatten(),
    'Predicted_Sales': future_preds
})

plt.figure(figsize=(14, 6))
plt.plot(monthly_sales['Date'], monthly_sales['Sales'], label='Ventas Reales')
plt.plot(monthly_sales['Date'], monthly_sales['Predicted_Sales'], label='Predicción (Entrenamiento)', linestyle='--')
plt.plot(future_df['Date'], future_df['Predicted_Sales'], label='Predicción Futura', linestyle='--', marker='o')
plt.title('Predicción de Ventas Mensuales')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()