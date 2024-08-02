import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'breadprice.csv'  # Make sure this file is in the same directory as this script
data = pd.read_csv(file_path)

# Calculate the average price for each year
data['AveragePrice'] = data.mean(axis=1)

# Extract the 'Year' and 'AveragePrice' columns
data = data[['Year', 'AveragePrice']]

# Sort the data by year just in case
data = data.sort_values(by='Year')

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data['AveragePrice'], marker='o')
plt.title('Average Price of Bread Over Years')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.show()
