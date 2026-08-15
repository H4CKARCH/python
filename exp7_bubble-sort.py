from array import *

def bubble_sort(list1, n):

    for j in range(len(list1) - 1):

        for i in range(len(list1) - 1):

            if list1[i] > list1[i + 1]:
                t = list1[i]
                list1[i] = list1[i + 1]
                list1[i + 1] = t

    return list1


ArraySize = int(input('Enter How many Elements to read: '))

list1 = array('i', [])

for i in range(ArraySize):
    list1.append(int(input()))

print('Sorted list is')

res = bubble_sort(list1, ArraySize)

for i in range(ArraySize):

    print(res[i])
