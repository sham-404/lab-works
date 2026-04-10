def min_max(arr):
    n = len(arr)

    if n == 1:
        return arr[0], arr[0]

    elif n == 2:
        return min(arr), max(arr)

    mid = n // 2

    l_min, l_max = min_max(arr[:mid])
    r_min, r_max = min_max(arr[mid:])

    return min(l_min, r_min), max(l_max, r_max)


arr = [4, 353, 3, 2525, 35, 252, 552, 5]
a, b = min_max(arr)
print("The min no is: ", a) 
print("The max no is: ", b)
