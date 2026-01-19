from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt


def linear_search(arr, elm):
    for idx, val in enumerate(arr):
        if val == elm:
            return idx
    return -1


x = []
y = []

for i in range(5):
    n = int(input("Enter the value of n: "))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(-1000, 1000)

    start_time = timer()
    idx = linear_search(arr, k)
    end_time = timer()

    elapsed_time = end_time - start_time
    y.append(elapsed_time)

plt.plot(x, y)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()
