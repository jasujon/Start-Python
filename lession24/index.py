#-----------------------------------Decorators------------------------------

#
#You have to have a complite understanding of functions 
#first class function / closures
#then we will learn about decorators
#


# def square(a):
#     return a**2
# # s=square(7)
# # print(s)

# #output : 49

# s = square
# # print(s(7))
# #output : 49            # same result 

# #find function name 
# print(s.__name__)
# #output : square
# print(s)                #for find location
# #output : <function square at 0x037F0340>
# print(square)           #for find location
# #output : <function square at 0x037F0340>




























#-----------------------------------Pass function as argument------------------------------


# #map function 
# def square(a):
#     return a**2
# l=[1,2,3,4,5]
# print(list(map(square,l)))              #take function as a argument
# #output : [1, 4, 9, 16, 25]             #square all the value


# def square(a):
#     return a**2

# l = [1,2,3,4,5]

# def my_map(func , l ):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

# print(my_map(square,l))
# #output : [1, 4, 9, 16, 25]





































#-----------------------------------Function returning function------------------------------

# def outer_func():
#     def inner_func():
#         print("This is Inner Function..")
#     return inner_func()     #when i return function
# var = outer_func()
#output : This is Inner Function..      # its not a function returning function


# def outer_func():
#     def inner_func():
#         print("This is Inner Function .. ")
#     return inner_func   # now don't return ()
# var = outer_func()
# #output: null

# var()
#output : This is Inner Function ..
































#-------------------Decorators Intro (enhance the functionality of other Function)---------------

#Decorators = enhance the functionality of other Function


#Decorators function
def decorators_function(any_function):
    def wrapper_function():
        print('This is Awesome Function .. ')
        any_function()
    return wrapper_function

#this is awesome function       
def func1():
    print('This is Function One')
#func1()
#output : This is Function One


#this is awesome function 
def func2():
    print('This is Function Two')
#func2()
#output : This is Function Two

var = decorators_function(func1)
var()
#output : This is Awesome Function ..
        #This is Function One