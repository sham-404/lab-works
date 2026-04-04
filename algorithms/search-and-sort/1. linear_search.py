from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt


def linear_search(arr, search):
    for idx, elm in enumerate(arr):
        if elm == search:
            return idx
    return -1


x = []
y = []

for i in range(5):
    n = int(input("\nEnter the value of n: "))
    x.append(n)

    arr = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(0, 1000)
    
    start = timer()
    linear_search(arr, k)
    end = timer()

    elapsed_time = end - start 
    y.append(elapsed_time)
    print(f"Time taken to search {k} in {n} elements: {elapsed_time} ")

plt.plot(x, y)
plt.title("Time taken for linear search")
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.show()
