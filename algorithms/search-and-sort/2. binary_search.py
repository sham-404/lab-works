import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def binary_search(arr, elm, low, high):
    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == elm:
        return mid

    elif arr[mid] > elm:
        return binary_search(arr, elm, low, mid - 1)

    else:
        return binary_search(arr, elm, mid + 1, high)


x = []
y = []


for i in range(5):
    n = int(input("\nEnter the value of n: "))
    x.append(n)

    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(0, 1000)
    
    start = timer()
    binary_search(arr, k, 0, n - 1)
    end = timer()

    elapsed_time = end - start 
    y.append(elapsed_time)
    print(f"Time taken to search {k} in {n} elements: {elapsed_time} ")

plt.plot(x, y)
plt.show()
