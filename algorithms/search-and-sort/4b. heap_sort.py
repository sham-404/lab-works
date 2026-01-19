import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


x = []
y = []

for i in range(5):
    n = int(input("Enter the value of n: "))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(-1000, 1000)

    start_time = timer()
    heap_sort(arr)
    end_time = timer()

    elapsed_time = end_time - start_time
    y.append(elapsed_time)

plt.plot(x, y)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()
