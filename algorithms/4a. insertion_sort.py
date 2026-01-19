import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def insertion_sort(arr):
    for step, elm in enumerate(arr[1:]):
        j = step - 1
        while j >= 0 and arr[j] > elm:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = elm


x = []
y = []

for i in range(5):
    n = int(input("Enter the value of n: "))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(-1000, 1000)

    start_time = timer()
    insertion_sort(arr)
    end_time = timer()

    elapsed_time = end_time - start_time
    y.append(elapsed_time)

plt.plot(x, y)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()
