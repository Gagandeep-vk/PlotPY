import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Categories': ['A', 'B', 'C', 'D'],
    'Values': [10, 15, 7, 25]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a bar graph
plt.bar(df['Categories'], df['Values'], color='skyblue')

# Add title and labels
plt.title('Bar Graph Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()
