import matplotlib.pyplot as plt
import numpy as np

# Training epochs
epochs = list(range(1, 21))

# CLRNet performance metrics data
mF1 = [49.14, 50.98, 51.70, 51.72, 52.08, 53.52, 53.20, 53.55, 54.56, 53.85,
       55.03, 54.91, 54.70, 55.01, 55.18, 55.31, 55.26, 55.41, 55.46, 55.41]

F1_50 = [74.75, 76.00, 76.97, 76.82, 77.47, 78.07, 78.33, 78.06, 78.34, 78.67,
        79.21, 79.28, 79.28, 79.35, 79.43, 79.56, 79.58, 79.66, 79.73, 79.65]

F1_75 = [55.20, 57.74, 58.25, 58.02, 58.49, 60.17, 60.56, 60.60, 61.64, 61.20,
        62.26, 62.14, 61.72, 62.15, 62.27, 62.36, 62.31, 62.44, 62.60, 62.51]

# Create figure and plot
plt.figure(figsize=(10, 6))

plt.plot(epochs, mF1, label='mF1', color='#1f77b4', linewidth=2, marker='o')
plt.plot(epochs, F1_50, label='F1_50', color='#ff7f0e', linewidth=2, marker='s')
plt.plot(epochs, F1_75, label='F1_75', color='#2ca02c', linewidth=2, marker='^')

# Customize the plot
plt.title('DG_CLRNet Performance on CULane Dataset', fontsize=14)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Score (%)', fontsize=12)
plt.xticks(epochs)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Save the figure
plt.savefig('dg_clrnet_performance_curves.png', dpi=300, bbox_inches='tight')
print("图像已保存为 dg_clrnet_performance_curves.png")

# Show the plot
plt.show()