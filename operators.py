OPERTAORS :
 
Operators used to perform operations on variables and values 
operands --> on which the operations are performed
operators --> special symbols used in opearion
 
OPERATORS IN PYTHON:
1.arithmetic
2.logical
3.Comparison
4.Bitwise
5.Assignment
6.Identity
7.Membership


ARITHMETIC:
---------------
  used to perform the basic mathematical calculations including +,-,*,/,%,**,//
  --> Normal division always results in float values
  --> Floor division results in float value if one of the value is a float value.
  Precedence order: B O E D M A S
  
RELATIONAL:
---------------
  used in comapring values and returns true or false
  The basic operators in relational are <,>,<=,>=,==,!=
  All the operators have the same precedence
  
LOGICAL:
-----------
  The operators of logical are AND,OR,NOT
  These operators are used combine the conditional statements
  AND: true if both are true
  OR: true if one of it is true
  NOT: true if false
  Precedence order: NOT>AND>OR
    
Bitwise:
------------
  used to operate on  binary numbers
  The operators are |,&,~,^,>>,<<
  Precedence order: NOT>SHIFT>AND>XOR>OR
    
Assignment:
----------------
  used to asssign values to the variables
  The opeartors include =,+=,-=,*=,/=,%=,**=,//=,&=,|=,^=,>>=,<<=
  
Identity:
-------------
  is and is not are the identity operators
  used to check if two values are located in same part of memory
  
Membership:
-------------
  in and not in are the two membership operators
  used to test whether a value is in a given sequence or not
  
Ternary:
-----------
  it evaluates an expression based on a condition
  [on_true]if[expression]else[on_else]

Any and all operators:
--------------------------
ANY:returns true if any one of the item is true
    else returns false false even if its empty
    
ALL:returns true if all are true or empty
  
  
OPERATOR FUNCTIONS:
---------------------
  To perform some of the mathematical opeartions we have some inbuilt functiins like add(),sub(),mul()   to use these operator functions we need to import operator module
  operator functions include truediv(a,b),floordiv(a,b),pow(a,b),mod(a,b),lt(a,b),le(a,b) etc..
    
