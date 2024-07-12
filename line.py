import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 5, 7, 11]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a line graph
plt.plot(df['X'], df['Y'], marker='o', color='blue', linestyle='-')

# Add title and labels
plt.title('Line Graph Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
