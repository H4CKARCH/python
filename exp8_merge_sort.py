from array import *

def merge(a, low, mid, high):
    i = low
    j = mid + 1
    temp = []

    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i = i + 1
        else:
            temp.append(a[j])
            j = j + 1

    while j <= high:
        temp.append(a[j])
        j = j + 1

    while i <= mid:
        temp.append(a[i])
        i = i + 1

    # Copying back values from temp array to main array
    k = low

    for z in temp:
        a[k] = z
        k = k + 1


def mergesort(a, low, high):
    if low < high:
        mid = (low + high) // 2

        mergesort(a, low, mid)
        mergesort(a, mid + 1, high)

        merge(a, low, mid, high)


list1 = array('i', [])

num = int(input('Enter How many Elements to read: '))

print("Enter", num, "elements")

for y in range(num):
    list1.append(int(input()))

mergesort(list1, 0, num - 1)

print("Sorted list is")

for y in range(num):
    print(list1[y], end=" ")
