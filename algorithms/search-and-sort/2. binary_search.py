from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt


def binary_search(arr, elm):
    high = len(arr) - 1
    low = 0

    while high > low:
        mid = (high + low) // 2

        if arr[mid] == elm:
            return mid

        elif arr[mid] > elm:
            high = mid - 1

        else:
            low = mid + 1
    return -1


x = []
y = []

for i in range(5):
    n = int(input("Enter the value of n: "))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(-1000, 1000)

    start_time = timer()
    idx = binary_search(arr, k)
    end_time = timer()

    elapsed_time = end_time - start_time
    y.append(elapsed_time)

plt.plot(x, y)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()
