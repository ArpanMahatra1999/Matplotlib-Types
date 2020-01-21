import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 8, 10]
y = [12, 16, 6]
plt.scatter(x, y, label='line one', color='k', s=25, marker='o')

plt.title('Simple PLot')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.legend()
plt.grid(True, color='k')
plt.show()
