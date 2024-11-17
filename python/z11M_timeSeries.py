import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Generate date range
start_date = '2023-01-01'
end_date = '2023-12-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate random values for the time series
values = np.random.randn(len(date_range))

# Create a DataFrame with date as index and values as a column
time_series_data = pd.DataFrame({'Date': date_range, 'Value': values})

# Plot the time series data
plt.figure(figsize=(10, 5))
plt.plot(time_series_data['Date'], time_series_data['Value'], label='Time Series Data')
plt.title('Simple Time Series Dataset')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Save the dataset to a CSV file
time_series_data.to_csv('z11_time_series_dataset.csv', index=False)
