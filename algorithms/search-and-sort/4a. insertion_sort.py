import random
from timeit import default_timer as timer 
import matplotlib.pyplot as plt 


def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


x = []
y = []

for i in range(5):
    n = int(input("\nEnter the value of n: "))
    x.append(n)

    arr = [random.randint(0, 1000) for _ in range(n)]
    
    start = timer()
    insertion_sort(arr)
    end = timer()

    elapsed_time = end - start 
    y.append(elapsed_time)
    print(f"Time taken to sort {n} elements: {elapsed_time} ")


plt.plot(x, y)
plt.title("Time taken for insertion sort")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()

