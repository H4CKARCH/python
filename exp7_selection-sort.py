from array import *

def selection_sort(lst1, n):

    for i in range(n - 1):
        mini = i

        for j in range(i + 1, n):
            if lst1[mini] > lst1[j]:
                mini = j

        t = lst1[i]
        lst1[i] = lst1[mini]
        lst1[mini] = t

    return lst1


ArraySize = int(input('Enter how many Elements to read: '))

list1 = array('i', [])

for k in range(ArraySize):
    list1.append(int(input()))

print('Sorted list is')

res = selection_sort(list1, ArraySize)

for k in range(ArraySize):
    print(res[k])
