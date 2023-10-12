import matplotlib.pyplot as plt
import numpy as np

# Define the quality gates and their criteria
quality_gates = ['Gate 1', 'Gate 2', 'Gate 3', 'Gate 4']
criteria = [80, 90, 95, 99]

# Create a radar chart
angles = np.linspace(0, 2*np.pi, len(quality_gates), endpoint=False)
criteria += criteria[:1]
angles += angles[:1]
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, criteria, 'o-', linewidth=2)
ax.fill(angles, criteria, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, quality_gates)
ax.set_title('Quality Gates')

# Show the plot
plt.show()
