import matplotlib.pyplot as plt

# Define the quality gates and their criteria
quality_gates = ['Gate 1', 'Gate 2', 'Gate 3', 'Gate 4']
criteria = [80, 90, 95, 99]

# Create a bar chart
plt.bar(quality_gates, criteria)
plt.xlabel('Quality Gates')
plt.ylabel('Criteria (%)')
plt.title('Quality Gates')

# Show the plot
plt.show()