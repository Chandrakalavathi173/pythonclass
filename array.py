ARRAYS:

Arrays are the continuous memory locations to store only homegenous data.
similar to the lists but the difference is only with the data types of the elements stored.
we can create an array using the array module
example

from array import *
arr=array('i',[1,2,3])          # 1 2 3
for i in arr:
    print(i)
    
   
import array as arr
a=arr.array('i',[1,2,3])         # 1 2 3
for i in a:
    print(i)

indexing is allowed in the arrays so accessing can be done easily.
slicing can be used in arrays too.
    
ARRAY METHODS:

1. insert() -- inserts the element at specified position
2. append() -- inserts element at the end of the array
3. pop() --removes the last element / if index is given removes that particular eleemnt
4. remove() --removes frst occurance of that element from array
5. index() --prints the index of frst occurance of the element
6. count() --counts the no.of occurances of the element
7. reverse() --reverses the array
8. extend() --adds the elememnts to the existing array


    

