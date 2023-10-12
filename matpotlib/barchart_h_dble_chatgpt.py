import matplotlib.pyplot as plt

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3']
values1 = [3.2, 6.5, 4.8]
values2 = [4.5, 7.2, 5.1]

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 5))
bar_width = 0.35  # Width of each bar
bar_positions1 = [i - bar_width/2 for i in range(len(groups))]  # Positions of the first bars
bar_positions2 = [i + bar_width/2 for i in range(len(groups))]  # Positions of the second bars

# Plotting the first set of bars
ax.barh(bar_positions1, values1, height=bar_width, color='red', label='Values 1')

# Plotting the second set of bars
ax.barh(bar_positions2, values2, height=bar_width, color='blue', label='Values 2')

# Customizing plot appearance
ax.set_xlabel('Values')
ax.set_ylabel('Groups')
ax.set_title('Horizontal Bar Chart with Two Bars for Each Group')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticks([i for i in range(len(groups))])  # Set custom y-ticks to align bars with group labels
ax.set_yticklabels(groups)  # Set group labels as y-tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=12)
ax.legend()  # Add legend

# Show the plot
plt.show()
