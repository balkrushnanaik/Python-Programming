import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 5]

plt.plot(x,y, marker='o', linestyle='--', color='b')
plt.title('Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()