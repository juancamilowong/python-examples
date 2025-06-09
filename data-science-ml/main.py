import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Dataset of monthly sales
data = {
    'month': np.arange(1, 13),
    'sales': [100, 120, 130, 150, 170, 160, 180, 200, 210, 230, 250, 270]
}
df = pd.DataFrame(data)

# 2. Data visualization
plt.plot(df['month'], df['sales'], marker='o')
plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 3. Train linear regresion model
X = df[['month']]  # All the features should be in a dataframe format
y = df['sales']
model = LinearRegression()
model.fit(X, y)

# 4. Predict next 3 months
future_months = np.array([[13], [14], [15]])
predictions = model.predict(future_months)

# 5. Show predictions
print("Future predictions:")
for month, pred in zip(future_months.flatten(), predictions):
    print(f"Month {month}: {round(pred)} sales")

# 6. Visualization with the predictions
plt.plot(df['month'], df['sales'], marker='o', label='History')
plt.plot(future_months, predictions, 'ro--', label='Prediction')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.title("Sales prediction")
plt.grid(True)
plt.show()
