import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# load the dataset
df = pd.read_csv('daily_temperature.csv')
# Convert the 'Date' column to datetime and sort the data
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# prepare dataset for Prophet
df_prophet = df.rename(columns={'Date': 'ds', 'Temperature': 'y'})

# select the New York data only
df_prophet = df_prophet[df_prophet['City'] == 'New York']

# Initialize and fit the model
model = Prophet(daily_seasonality=True)
model.fit(df_prophet)

# Make a dataframe for predictions
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)

# Merge the forecast with the original data
df_prophet.set_index('ds', inplace=True)
forecast.set_index('ds', inplace=True)
df_merged = df_prophet.join(forecast[['yhat', 'yhat_lower', 'yhat_lower', 'yhat_upper']], how='inner')

# Calculate MAE
y_test = df_merged['y']
predictions = df_merged['yhat']
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')


# Reset the index for plotting purposes
df_merged.reset_index(inplace=True)

# Plot the actual vs predicted temperatures
plt.figure(figsize=(10, 6))
plt.plot(df_merged['ds'], df_merged['y'], 'b-', label='Actual Temperature', marker='o', markersize=8)
plt.plot(df_merged['ds'], df_merged['yhat'], 'r-', label='Predicted Temperature', marker='o', markersize=8)

for i, txt in enumerate(df_merged['y']):
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['y'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df_merged['yhat']):
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['yhat'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# run the functions
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Actual vs. Predicted Temperatures')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Python program that uses machine learning to predict temperatures, and successfully utilized time #series prediction.

#MAE measures the average absolute difference between actual and predicted values — lower is better
#Unlike RMSE, MAE treats all errors equally regardless of size, making it less sensitive to outliers
#Prophet's yhat is the median prediction, so MAE here tells you how many degrees off the model #typically is