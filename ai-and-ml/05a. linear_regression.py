import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

x_mean = np.mean(x)
y_mean = np.mean(y)

b_yx = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
a_yx = y_mean - b_yx * x_mean

y_pred = a_yx + b_yx * x

b_xy = np.sum((x - x_mean) * (y - y_mean)) / np.sum((y - y_mean) ** 2)
a_xy = x_mean - b_xy * y_mean

x_pred = a_xy + b_xy * y

print(f"Regression line of y on x: y = {a_yx:.2f} + {b_yx:.2f}x")
print(f"Regression line of x on y: x = {a_xy:.2f} + {b_xy:.2f}y")

plt.figure(figsize=(8, 6))

plt.scatter(x, y, color='blue', label='Data Points')

plt.plot(x, y_pred, color='green', label='Regression line of y on x')

sorted_y = np.sort(y)
sorted_x_pred = a_xy + b_xy * sorted_y

plt.plot(
    sorted_x_pred,
    sorted_y,
    color='red',
    label='Regression line of x on y'
)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Regression Lines and Data Points')
plt.legend()
plt.grid(True)
plt.show()
