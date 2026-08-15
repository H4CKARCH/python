from array import *

def partition(x, low, high):
    pivot = x[high]
    i = low - 1

    for j in range(low, high):
        if x[j] <= pivot:
            i = i + 1

            t = x[i]
            x[i] = x[j]
            x[j] = t

    t = x[i + 1]
    x[i + 1] = x[high]
    x[high] = t

    return i + 1


def quicksort(x, low, high):
    if low < high:
        p = int(partition(x, low, high))

        quicksort(x, low, p - 1)
        quicksort(x, p + 1, high)

    return x


list1 = array('i', [])

n = int(input('Enter How Many Elements To Read: '))

for i in range(n):
    list1.append(int(input()))

print('Stored list is:')

for i in range(n):
    print(list1[i], end=" ")

print()

res = quicksort(list1, 0, n - 1)

print('Sorted list is:')

for i in range(n):
    print(res[i], end=" ")
