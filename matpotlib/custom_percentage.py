import matplotlib.pyplot as plt

# Generate some example data
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Set the x-axis tick locations and labels
tick_locs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
tick_labels = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']
ax.set_xticks(tick_locs)
ax.set_xticklabels(tick_labels)

# Set the x-axis label
ax.set_xlabel('Percentage')

# Set other labels and title
ax.set_ylabel('Values')
ax.set_title('Plot with Custom Percentage Tick Labels')

# Display the plot
plt.show()
