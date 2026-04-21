import matplotlib.pyplot as plt
import numpy as np

try:
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 5]

    plt.scatter(x, y, color='r', marker='x')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    
except Exception as e:
    print(f"An error occurred: {e}")