import matplotlib.pyplot as plt

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3']
values = [3.2, 6.5, 4.8]

# Define color conditions using a list comprehension
colors = ['red' if value < 5 else 'orange' if 5 <= value < 7 else 'green' for value in values]

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(groups, values, color=colors)

# Customizing plot appearance
ax.set_xlabel('Values')
ax.set_ylabel('Groups')
ax.set_title('Horizontal Bar Chart with Color Conditions')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(fontsize=10)
plt.yticks(fontsize=12)

# Show the plot
plt.show()
