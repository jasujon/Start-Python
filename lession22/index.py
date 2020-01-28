#------------------------------------Lambda Expression (anonymous function)-----------------------------


#lambda expression / anonymous function means this function don't  have name


#normal function
# def add (a,b):
#     return a+b


#lambda Expression / anonymous function
# add2 = lambda a,b : a+b
# print(add2(5,3))
# #output : 8
# print(type(add2))
# #output : <class 'function'>


# multiply = lambda a,b : a*b 
# print(multiply(5,5))
# #output : 25


# print(add2)
#<function <lambda> at 0x00E80388>              # lambda and location show






















#------------------------------------Lambda Expression Practice-----------------------------

#normal function
# def is_even(a):
#     if a % 2 == 0 :
#         return True
#     else:
#         return False
# print(is_even(5))
# #output : 5


#shorted function in is_even function :

# def is_even(a):
#     return a % 2 == 0 
# print(is_even(4))
#output: True



#Lambda Expression use this function

is_even = lambda a : a % 2 == 0
print(is_even(10))
#output : True




