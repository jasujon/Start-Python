#-----------------------------------Decorators------------------------------

#
#You have to have a complite understanding of functions 
#first class function / closures
#then we will learn about decorators
#


def square(a):
    return a**2
# s=square(7)
# print(s)

#output : 49

s = square
# print(s(7))
#output : 49            # same result 

#find function name 
print(s.__name__)
#output : square
print(s)                #for find location
#output : <function square at 0x037F0340>
print(square)           #for find location
#output : <function square at 0x037F0340>