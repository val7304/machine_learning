import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3']
values1 = [10, 30, 20]
values2 = [5, 25, 15]
values3 = [15, 20, 10]

# Condition colors
colors = np.array([[0.2, 0.5, 0.8],
                   [0.4, 0.7, 0.2],
                   [0.8, 0.2, 0.5]])

# Create figure and axes
fig, ax = plt.subplots()

# Create stacked bar chart with condition colors
bar_width = 0.35
bar1 = ax.bar(categories, values1, bar_width, color=colors[0])
bar2 = ax.bar(categories, values2, bar_width, color=colors[1], bottom=values1)
bar3 = ax.bar(categories, values3, bar_width, color=colors[2], bottom=np.array(values1)+np.array(values2))

# Create color bar legend
cax = fig.add_axes([0.93, 0.2, 0.03, 0.6])  # [left, bottom, width, height]
cbar = plt.colorbar(ax.contourf([[0, 0], [0, 0]], colors=colors), cax=cax)
cbar.set_ticks([0.25, 0.5, 0.75])
cbar.set_ticklabels(['Condition 1', 'Condition 2', 'Condition 3'])

# Create custom legend
bar_handles = [bar1[0], bar2[0], bar3[0]]
label1 = 'Value 1'
label2 = 'Value 2'
label3 = 'Value 3'
legend1 = ax.legend(bar_handles, [label1, label2, label3], loc='upper left')
ax.add_artist(legend1)

# Set title and labels
ax.set_title('Condition Color Bar Chart with Double Legend')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Show the plot
plt.show()
