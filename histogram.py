import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 8, 10, 12, 9, 7, 4]
y = [0, 10, 20]
plt.hist(x, y, histtype='bar', rwidth=0.5)

plt.title('Simple PLot')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.legend()
plt.grid(True, color='k')
plt.show()
