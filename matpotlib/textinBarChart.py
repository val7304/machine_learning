import matplotlib.pyplot as plt

# Define the quality gates and their criteria
quality_gates = ['Gate 1', 'Gate 2', 'Gate 3', 'Gate 4']
criteria = [80, 90, 95, 99]

# Define a new variable and its values for each quality gate
new_variable = ['Var A', 'Var B', 'Var C', 'Var D']
values = [15, 20, 10, 30]

# Define the status for each quality gate (for this example, we'll just assume that Gates 1 and 3 have an "ERROR" status)
status = ['OK', 'ERROR', 'OK', 'ERROR']

# Define colors for each status
colors = ['green' if s == 'OK' else 'red' for s in status]

# Create a bar chart
fig, ax = plt.subplots()
rects1 = ax.bar(quality_gates, criteria, color=colors)
ax.set_xlabel('Quality Gates')
ax.set_ylabel('Criteria (%)')
ax.set_title('Quality Gates')

# Add the new variable values to the bars
for i, rect in enumerate(rects1):
    ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2, f"{new_variable[i]}: {values[i]}", ha='center', va='bottom')

# Add a legend to the graph
ax.legend(handles=[plt.Rectangle((0,0),1,1,color='green'), plt.Rectangle((0,0),1,1,color='red')], labels=['OK', 'ERROR'])

# Show the plot
plt.show()