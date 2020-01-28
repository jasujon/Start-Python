#------------------------------------Enumerate function-----------------------------  

#
# we use enumerate function with for loop to track position of our item in iterable
#
 


 #
 #How we can do this without enumerate function
 #

# names = ['Jubayed','Alam','Sujon']
 # suppose we need our result like this :  0 ---> Jubayed , 1---> Alam

# position = 0
# for name in names :
#     print(f"{position} ---- > {name}")
#     position += 1
#output: 
# 0 ---- > Jubayed
# 1 ---- > Alam
# 2 ---- > Sujon



#
#with enumerate function
#
# for position,name in enumerate(names):
#     print(f"{position} ---- > {name}")
#output : 
# 0 ---- > Jubayed
# 1 ---- > Alam
# 2 ---- > Sujon

























#------------------------------------Map function-----------------------------  

# numbers = [1,2,3,4,5]

# #
# # without lambda
# #
# def square(a):
#     return a**2
# square1 = list(map(square,numbers))         # number convert list 
# print(square1)
# #output : [1, 4, 9, 16, 25]


# #
# # with lambda
# #
# square = list(map(lambda a: a**2 , numbers))
# print(square)
# #output : [1, 4, 9, 16, 25]



































#------------------------------------Filter Function----------------------------- 

#
# show just even number
#

numbers = [1,2,4,6,8,35,76,6]

def is_even(a):
    return a % 2 == 0

even = tuple(filter(is_even,numbers))
print(even)

#output : (2, 4, 6, 8, 76, 6)