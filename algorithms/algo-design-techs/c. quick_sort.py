import random
from time import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

x, y = [], []

for _ in range(3):
    n = int(input("enter the value of n: "))
    x.append(n)

    arr = [random.randint(0, 1000) for _ in range(n)]
    print("\nThe array elements are", arr)

    start = time()
    quick_sort(arr, 0, n - 1)
    elapsed = time() - start

    print("array elements are", arr)
    print("time taken =", elapsed)

    y.append(elapsed)

plt.plot(x, y)
plt.title("Time Taken for quick sort")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()


