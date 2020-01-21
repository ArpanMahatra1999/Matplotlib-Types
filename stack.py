import matplotlib.pyplot as plt

u = [1, 2, 3, 4, 5]
x = [7, 8, 6, 11, 7]
y = [2, 3, 4, 3, 2]

plt.plot([], [], color='m', label='x', linewidth=2)
plt.plot([], [], color='c', label='y', linewidth=2)
plt.stackplot(u, x, y, colors=['m', 'c'])

plt.title('Simple PLot')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.legend()
plt.show()
