#------------------------- oop intro(Object Oriented Programing)-------------------------


#object oriented programing
#common topic in almost all popular programing language (python , javaScript, Php , c,C++) with common      idea but different syntex
# oop just style or way to write a code
# oop very helpful to creating real world programs
# 
# 
# 
# we hearing many time in oop like 1. Class 2. Object(instance) 3. Method
# 
# 
# list class
# list object
# list method
# 
# i = [1,2,3,4,5]
# i.append(d)           # hear append is a method
#
#And i in class Object





















#-------------------------------- OOP Create Your First Class-----------------------------------
#
#
#how to create an class
#what is Init Method    # we also callled constructor in PHP
#what are ATTRIBUTES , INSTANCE VARIABLES
#how to create our object
# 
#  

class Person:
    def __init__(self, first_name,last_name,age):
        #instance variable
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

#create object

p1 = Person('Jubayed','Alam',25)
print(p1.first_name)
#output : Jubayed
p2 = Person('Israk','Jahan',17)
print(p2.last_name)
#output : jahan
