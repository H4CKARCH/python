from array import * 
def linear_Search(list1, n, key): 
 # Searching list1 sequentially 
 for i in range(0, n): 

     if (list1[i] == key): 

         return i 
 return -1 
ArraySize = int(input('Enter How many Elements to read:')) 
list1 = array('i', []) 
for i in range(ArraySize): 
 print("Enter ",str(i+1),"Element") 
 list1.append(int(input())) 
key = int(input('Enter Key:')) 
# Function call 
n=int(len(list1)-1) 
res = linear_Search(list1, n, key) 
if res != -1: 
 print("Element is present at index", str(res)) 
else: 
 print("Element is not present in list")
