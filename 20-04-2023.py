STRINGS:


String is a sequence of characters represented using the quotes.
Example:

name="Chandu"
print(type(name))

Indexing can be used to access the each element in the string.

name="Chandu"
print(name[2])  #a

print(name[-3])  #n    [negative indexing: Starts from end and frst index represented with -1]

 STRING SLICING:
 
 String slicing is used to print a part of string strting from any index.
 it requires 3 arguments start index, end index and step value.(step value is optional amd default is 1)
 
 name="Chandrakalavathi"
 print(name[2:8])  #andrak
 print(name[3:9:2])  #nrk
 print(name[9:4:-1)   #lakar
 #To print reverse of a string
 print(name([::-1])   #reverse of string will be printed
 STRING CONCATENATION HAPPENS USING TO "+" operator
 
 ESCAPE SEQUENCING:
 
print('I am a "human"')             I am a "human"
print("I am a 'human'")             I am a 'human'
print('''I am a "human"''')         I am a "human"
print('I am a \'human\'')           I am a 'human'
print("I am a \"human\"")           I am a "human"
print('I am a \t\t\thuman')         I am a    human
print('I am a \nhuman')             I am a 
                                    human
 
For UPDATION join funtion can be used
 
a="abcd"
list1=list(a)          #abyd
list1[2]="y"
print("".join(list1))

for DELETION using slicing 

a="abcdefg"
b=a[:3]+a[4:]          #abcefg
print(b)
 
 complete string DELETION 
 
 a="abcd"
 print(a)          #abcd
 del a
 print(a)          #NameError
 
 
 STRING METHODS:
 
 1. endswith()  --returns true if string end with the f\given character/string.
 2. startswith() --returns true if it starts with the given argument.
 3. isdigit() -- returns true if string is digit (no arguments taken)
 4. isalpha() --returns true if string is alphabets
 5. index() --frst occurence of the character
 6. upper() --converts all characters into uppercase
 7. lower()-- conversts all characters into lowercase
 8. strip() --removes leading and trailing white spaces
 9. replace() --rplaces the old substring with new one (aruments : old,new)
 10. capitalize -- capitalizes the frst cahracter of the word
 11. isdecimal -- returns true if all are decimals
 12. swapcase() --converts upper to lower and viceversa
 13. len(argument) -- returns length of the string
 14. index,rindex --returns the lowest index of the element,returns the highest index
 15. find,rfind   --returns the lowest index of the element,returns the highest index
 16.count() --counts the number of occurences of the element
 17. join() --joins the list tuples
 
 
 EXAMPLE CODE SNIPPETS FOR STRING METHODS:
 
 
 # startswith
var="pythonprogramming"
print(var.startswith("y"))

# endswith
var="pythonprogramming"
print(var.endswith("g"))

# isdigit or isdecimal
var="pythonprogramming"
print(var.isdigit())

# isalpha
var="pythonprogramming"
print(var.isalpha())

# isalnum
var="pythonprogramming123"
print(var.isalnum())

# upper
var="pythonprogramming"
print(var.upper())

# lower
var="PYTHONPROGRAMMING"
print(var.lower())

# swapcase
var="pythonPROGRAMMING"
print(var.swapcase())

# replace
var="pythonprogramming"
print(var.replace("python","java"))

# len
var="pythonprogramming"
print(len(var))

# index,rindex
var="pythonprogramming"
print(var.index("n"))
print(var.rindex("n"))

# capitalize
var="python programming"
print(var.capitalize())

# find,rfind
var="pythonprogramming"
print(var.find("n"))
print(var.rfind("n"))

# count
var="pythonprogramming"
print(var.count("n"))

# join
var="abc"
var1="def"
print(var.join(var1))

var="abc"
var1="def"
print("".join([var,var1]))

# strip
var="   abc    "
print(var.strip())
print(var.lstrip())
print(var.rstrip())


 
 ------------------------------------------------------------------------------------------------------------------------------------------------------
 
 LISTS:
 
 List is a datatype which stores data of different datatypes(heterogeneous)
 it is a mutable datatype
 
 CREATION OF LISTS:
 
 list1=[1,2,"abc",10.998798]
 print(type(list1))
 
 var=[]
 print(type(var))
 
 var=[1,2,3]
 print(var)

 the elemnts accesssed using indexes.
 
 INDEXING:
 
 var=[1,2,3,"python"]
 print(var[0],var[2],var[3])

 duplicates are allowed in the list.
 
 DUPLICATES:
 
 var=[1,2,3,"python",3,"c",2,1,"c"]
 print(var)
  
 MULTIDIMENSIONAL LISTS:
  
 var=[[1,2,3],["python","c","java"]]
 print(var[0])
 print(var[1])
 print(var[0][2])
 print(var[1][1])
 
 when input is taken using the split() function it returns the items stored in a list
 
 TAKING INPUT FOR LIST USING SPLIT FUNCTION:
 
 var=input().split()
 print(var)
 
 USING MAP FUNCTION:
 
 lst = map(int, input().split())
 var=list(lst)
 print(type(var[1]))
 
 LIST METHODS:
 
 1.len() --gives the length of list
 2.append() --adds new elemnt to the end of list  (a list or a tuple can also be appended to an existing an list)
 3.insert() --adds the element at specified position
 4.extend() --adds multiple elemnts into existing list
 5.reverse() --reverses the list and displays
 6.remove() --removes specific item from the list (only one element at a time)
 7.pop() --removes last element (to pop specific element argument is index) ----returns the popped element always
 8.clear() --clears the list
 9.index() -- returns index of frst occurance
 10.sort() --sorts the list in ascending order and descending order if reverse is given "true"
 11.copy() --copies the lsit into other
 12.count() --count the no.of occurrences
 
 
EXAMPLE CODE SNIPPETS FOR LIST METHODS:
 
# len
var=[1,2,3,"c","java","python"]
print(len(var))


# append
var=[1,2,3,"c","java","python"]
var.append("c++")
print(var)

# insert
var=[1,2,3,"c","java","python"]
var.insert(3,"c++")
print(var)

# extend
var=[1,2,3,"c","java","python"]
var.extend(["c++",4,5,"sql","html"])
print(var)

# reverse
var=[1,2,3,"c","java","python"]
var.reverse()
print(var)

# remove
var=[1,2,3,"c","java","python"]
var.remove("c")
print(var)

# pop
var=[1,2,3,"c","java","python"]
print(var.pop())
print(var)

# clear
var=[1,2,3,"c","java","python"]
var.clear()
print(var)

# index
var=[1,2,3,"c","java","python","c"]
print(var.index("c"))

# sort
var=[1,2,3,1,7,3,2,6,8]
var1=["c","python","sql","java"]
var.sort()
var1.sort()
print(var)
print(var1)

# count
var=[1,2,3,"c","java","c","python","c"]
print(var.count("c"))

# copy
var=[1,2,3,"c","java","python"]
var1=var.copy()
print(var1)
 
LIST COMPREHENSIONS:

Used to create new list from other iterable like string tuple list etc..
syntax:
lst=[x for x in range(1,11) if x%2==0)

# list comprehension
var=[x**2 for x in range(1,11)]
print(var)

var=[x**2 for x in range(1,11) if x%2==0]
print(var)
 
 ---------------------------------------------------------------------------------------------------------------------------
 
 TUPLES:
 Similar to list but immuatable'
 stores various data 
 to convert into tuple tuple() method can be used
 index can be used
 only difference between lists and tuples is that tuples are immutable
 
 CREATION:
 # empty tuple
tup=()
print(type(tup))

# not a tuple
tup=(2)
print(type(tup))
print(tup)

# single element tuple
tup=(2,)
print(type(tup))

# multiple data type 
tup=(1,2,"c")
print(type(tup))

# using built in function
tup=tuple("123")
print(type(tup))
print(tup)

# nested tuples
tup1=(1,2,3)
tup2=("c","c++","python")
tup3=(tup1,tup2)
print(tup3)

# tuple repetition
tup1=("python",)*3
print(tup1)

ACCESSING OF TUPLE ELEMENTS:

# Accessing of elements using indexing
tup1=(1,2,3,"c","python")
print(tup1[3])

# using unpacking
tup1=(1,2,3,"c","python")
a,b,c,d,e=tup1
print(a,b,c,d,e)

CONCATENATION OF TUPLES:

# concatenating
tup1=(1,2,3)
tup2=("c","c++")
print(tup1+tup2)

SLICING OF TUPLES:

# slicing
tup=(1,2,3,4,4,5,6,7,8,9)
print(tup[4:])
print(tup[-1])
print(tup[-1::-1])
 
 TUPLE METHODS:
 
 1.len()
 2.max()
 3.min()
 4.sorted(argument)
 5.sum()
 6.index()
 7.count()
 8.all()
 9.any()
 10.tuple() built in function
 
EXAMPLE CODE SNIPPETS:
 
# indexing
tup=(1,2,3,4,"c","python")
print(tup.index("python"))

# count
tup=(1,2,"c",3,"c",4,"c","python")
print(tup.count("c"))

# all and any
tup=(1,2,3,4,"c","python")
tup1=()
print(all(tup))
print(any(tup1))

# len
tup=(1,2,3,4,"c","python")
print(len(tup))

# max min sum
tup=(1,2,3,4)
print(max(tup),min(tup),sum(tup))

# sorted
tup=(1,2,3,4,2,6,9,3,6,9,1)
print(sorted(tup))
 
 
 
 
 
 
 
 
 
