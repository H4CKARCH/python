from array import *

def binary_search(ls, n):
    low = 0
    high = len(ls) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if ls[mid] < n:
            low = mid + 1

        elif ls[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1


# Initial list
ArraySize = int(input('Enter How many Elements to read: '))

list1 = array('i', [])

for i in range(ArraySize):
    print("Enter", str(i + 1), "Element")
    list1.append(int(input()))

# IMPORTANT: Binary search requires sorted data
list1 = array('i', sorted(list1))

print("Sorted list:", list1)

key = int(input('Enter Key: '))

# Function call
res = binary_search(list1, key)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in list")
