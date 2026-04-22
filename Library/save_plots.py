# import matplotlib.pyplot as plt # type: ignore

# x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# y = [5, 10, 12, 20, 25, 18, 35, 40, 20, 50]

# plt.bar(x, y, color='g', width=1.5, edgecolor='black')
# plt.title('Bar Chart')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.savefig('bar_chart.png')
# plt.show()

import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

months = np.arange(1, 13)
sales = [100, 150, 200, 250, 300, 350, 400, 50, 500, 550, 60, 50]

plt.plot(months, sales, marker='o', color='b', linestyle='--', linewidth=2)
plt.title('Monthly Sales')
plt.xlabel('Months')

plt.ylabel('Sales')
plt.style.use('fast')
plt.savefig('monthly_sales.png')
plt.show()