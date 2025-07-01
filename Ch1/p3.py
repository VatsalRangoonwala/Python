# Install an external module and use it to perform an operation of your interest.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 7]

# Create a line plot
plt.plot(x, y, marker='o', color='blue', linestyle='--')

# Add labels and title
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.grid(True)
plt.show()