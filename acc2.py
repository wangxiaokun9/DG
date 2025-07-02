import matplotlib.pyplot as plt
import numpy as np

# Training epochs
epochs = list(range(1, 21))

# CLRNet performance metrics data

F1_50 = [70.62, 71.51, 71.87, 71.47, 72.37, 73.04, 73.38, 73.98, 73.87, 73.77,
        74.25, 74.57, 74.67, 74.78, 74.90, 74.88, 74.63, 74.80, 74.88, 74.87]


# Create figure and plot
plt.figure(figsize=(10, 6))

plt.plot(epochs, F1_50, label='F1_50', color='#ff7f0e', linewidth=2, marker='s')


# Customize the plot
plt.title('DG_CLRNet Performance on CULane Dataset(Night)', fontsize=14)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Score (%)', fontsize=12)
plt.xticks(epochs)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Save the figure
plt.savefig('dg_clrnet_performance_Night_curves.png', dpi=300, bbox_inches='tight')
print("图像已保存为 dg_clrnet_performance_Night_curves.png")

# Show the plot
plt.show()