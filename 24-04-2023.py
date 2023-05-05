FUNCTIONS:

Advantages:
1. Readability
2. Reusability
3. clean and light weight

Syntax:
def function_name:
  #block of code
  
  Example:
  
  def add():
  a=10
  b=20
  c=a+b
  print(c)
add()
-------------------------------------
def add():
  a=int(input())
  b=int(input())        #Exception of value error occurs when string are given as input
  print(a+b)
add()
----------------------------------------
def add():
    try:
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    print(a+b)
add()
-------------------------------------------
def add():
  a=int(input())
  b=int(input())
  return (a+b)
add()
------------------------------------------
Using arguments and parameters

def add(a,b):     #arguments
  return a+b
print(add(30,40))   #parameters
------------------------------------------
Functions return multiple values

def multipleValues():
  return 10,20,30
print(multipleValues())       #returns numbers in a tuple format
-----------------------------------------------
Fibonocci series:

def fibonacci():
  n=int(input())
  if n<0 or n==0:
    print("Invalid")
  elif n==1:
    print(0)
  elif n==2:
    print(0," ",1
  else:
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(0,n-2):
      c=a+b
      print(c,end=" ")
      a=b
      b=c
fibonacci()
----------------------------------------------------
RECURSION:

def doJob(n):
    if n<=5:
        return 
    doJob(n-1)
    print(n)
    doJob(n-1)
    print(n)
doJob(8)
-----------------------------------------------------
def doJob():
  if n<=2:
    return
  print(n)
  doJob(n-1)
  print(n)

  
