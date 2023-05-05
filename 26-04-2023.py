OBJECT ORIENTED PROGRAMMING:

Creation of a class:

CONSTRUCTER:
Constructer will be executed before creation of an object.
DESTRUCTER:
destructor will be executed just before destruction of an object
-------------------------------------------------------------------------------
PROPERTIES OF OBJECT ORIENTED PROGRAMMING:
1.Inheritance
2.Polymorphism
3.Abstraction
4.Encapsulation
-------------------------------------------------------------------------------
INHERITANCE:
Child class will have access to the parent propertiess but the viceversa isn't possible.

EXAMPLES:

class Book:
    numberOfPages = 145
    author = "sudhanshu"
    scope = "To be sold in india"

    def __init__(self , zone , dob):
        self.zone = zone
        self.dob = dob                                          #sudhanshu
    def __del__(self):                                           25-10-1998
        print("destructor is called")                            Destructor is called

my_book = Book("Mystery","25-10-1998")
print(my_book.zone)
print(my_book.dob)
del my_book
---------------------------------------------------------------------------------------------------
