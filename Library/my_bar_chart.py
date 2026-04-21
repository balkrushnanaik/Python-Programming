import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [5, 10, 12, 20, 25, 18, 35, 40, 20, 50]

plt.bar(x, y, color='g', width=1.5, edgecolor='black')
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
