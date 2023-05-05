#dictionaries
#sets
#recursion(problem statements) --Tower of Hanoi problem
#Object oriented programming
--------------------------------------------------------------------------
Recursion

def fun(n):
  if n<=10:
    return                  
  print(n-1)                 #12 11 10 10 11 12 
  f(n-1)                     time complexity:O(n) -- linear
  print(n-1)
----------------------------------------------------------------------------
nth Fibonacci term (using recursion)

def nthfibonocci(n):
    if n==0:
        return -1
    if n==1:                                             #34
        return 0
    if n==2:
        return 1
    return nthfibonocci(n-1)+nthfibonocci(n-2)
print(nthfibonocci(10))
------------------------------------------------------------------------------
sum of n fibonocci terms:

def sumofnfibonocci(n):
  if n<=0:
    return -1
  if n==1:
    return 0
  if n==2:
    return 1
  a=0
  b=1
  res=a+b
  for i in range(0,n-2):
    c=a+b
    res=res+c
    a=b
    b=c
  print(res)
sumofnfibonocci(5)
---------------------------------------------------------------------------------
sum of n fibonocci terms (using recursion)

def sumofnfibonocci(n):



















--------------------------------------------------------------------------------------------------------------------------------------------------------------------
DICTIONARIES:

Dictionary is a collection of key value pair.
it stores the data in the form of key value pairs, while other datatypes store only single element.

CREATION:

Values in a dictionary can be of any type and duplicates are allowed but where as keys are immuatble and duplicate keys not allowed.
Also keys are case sensitive.

# CREATION

# empty dict1
dict1={}
print(dict1)

# dict with same datatype keys
dict1={1:"c",2:"python",3:"c++"}
print(dict1)

# dict with different datatype keys
dict1={1:"c","name":"Kavya","marks":20}
print(dict1)

# using built in function
dict1=dict({1:"dds",2:"dwa","name":"dsc"})
print(dict1)

# nested dictionaries
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1)

ADDING ELEMENTS INTO DICTIONARY:

# ADDING ELEMENTS INTO DICT
dict1={}
dict1[0]="abc"
dict1[1]="def"
dict1["name"]="kavya"
dict1["marks"]=20
print(dict1)

ACCESSING ELEMENTS OF DICTIONARY:

# ACCESSING OF ELEMENTS
# using key
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1[2])
print(dict1[3])


# using get method
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.get(2))

# for nested dictioanry
print(dict1[3]["B"])
print(dict1[3]["c"])

DELETION:

# DELETION
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
del dict1[2]
print(dict1)

METHODS OF DICTIONARIES:
1.clear() -- removes all elements
2.copy() --copies the dictionary
3.items() --returns key value pair in the form of tuples
4.keys() --returns all the keys
5.values() --returns all the values
6.pop() --removes and returns the spescified elmemnt
7.popitem() --removes last key value pair

EXAMPLE CODE SNIPPETS:

# METHODS OF DICTIONARIES:

# clear
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
dict1.clear()
print(dict1)

# copy
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
dict2=dict1.copy()
print(dict2)

# items
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.items())

# keys
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.keys())

# values
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.values())

# pop
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.pop(2))

# popitem
dict1={1:"abc",2:"def",3:{"A":"python","B":"java","c":"c++"}}
print(dict1.popitem())


-----------------------------------------------------------------------------------------------------------------------------------------------

SETS:

1. sets are unordered and unindexed
2.sets do not allow duplicate elements
3.sets are mutable
example:

arr=[1,2,1,4,3,4,2,3,4]
set1=set(arr)

CREATION:
Duplicate values may be passed during creation
Order is not defined in sets

# empty set
set1={}
print(set1)

set1=set()
print(set1)

# set with elements
set1={"Geek","For", "Geeks", "f",1,4,3,3,4,1,"F"}
print(set1)

set1=set("Geek For Geeks")
print(set1)

string="Geeks"
print(set(string))

ACCESSING OF SET ELEMENTS:
Cannot be accessed using index
1. using loops
2.using in keyword

# ACCESSING OF SET ELEEMNTS
set1={1,2,3,3,2,1,"c","python","c","c"}
for i in set1:
    print(i,end=" ")

print("Geeks" in set1)

METHODS OF SETS:

1.add() --adds an element into the set
2.update() --adds multiple eleemnts into the set
3.remove() or discard() --removes an element from the set but araises key error if element doesnt exist  / discard also removes an element but doesnt get changedd if element doesnt exist
4.pop() --removes the last elemnt and returns the elemnt
5.clear() --removes all the elements
6.copy() --copies the set into other

# add
set1={1,2,3,3,2,1,"c","python","c","c"}
set1.add("data structures")
print(set1)

# update
set1={1,2,3,3,2,1,"c","python","c","c"}
set1.update([5,6,7],[56,43],(76,32,(12,23)))
print(set1)

# remove or discard
set1={1,2,3,3,2,1,"c","python","c","c"}
set1.remove(2)
set1.discard(1)
set1.remove(3)
set1.remove("c")
set1.discard("python")
print(set1)
set1.discard(4)

# pop 
set1={1,2,3,3,2,1,"c","python","c","c"}
print(set1.pop())

# clear
set1={1,2,3,3,2,1,"c","python","c","c"}
set1.clear()
print(set1)

# copy
set1={1,2,3,3,2,1,"c","python","c","c"}
set2=set1.copy()
print(set2)

FROZEN SET:

--->Frozen set is an immutable version of set object.
--->in sets the elements can be modified but frozen sets can be modified after creation

# frozen set
set1={1,2,3,3,2,1,"c","python","c","c"}
set2=frozenset(set1)
print(set2)
set2.add(8)        # frozen set cannot be modified
print(set2)

MATHEMATICAL OPERTAIONS ON SETS:

1.union() --returns union of two sets
2.intersection() --returns intersection of two sets
3.difference() -- retruns the difference of two sets
4.isdisjoint() --returns true if two sets are disjoint

# MATHEMATICAL CALCULATIONS
# union
set1={1,2,3,3,2,1,"c","python","c","c"}
set2={2,9,4,"c","c++","java"}
print(set1.union(set2))
# difference
print(set1.difference(set2))
# intersection
print(set1.intersection(set2))
# isdisjoint
print(set1.isdisjoint(set2))


































































--------------------------------------------------------------------------------------------------------------
DICTIONARIES:
  
