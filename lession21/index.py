#------------------------------------Intro to *args / *operator-----------------------------


#  *operator
#  *args
#data gather tuple


#normal function 

# def total(a,b):
#     return a+b
# print(total(2,3))
#output : 5 

#but if we try to pass many argument
#### print(total(3,4,6))
####output : TypeError: total() takes 2 positional arguments but 3 were given


#if we try to pass many argument in my function than we can use *args or *operator

# def total(*args):
#     print (args)
# #output : (1, 2, 3, 4, 5)
#     print(type(args))
# #output : <class 'tuple'>
# total(1,2,3,4,5)



# * args loop function
# def all_total(*args):
#     total = 0
#     for num in args :
#         total  += num
#     return total
# print(all_total(1,2,3))
#output : 6
























#-----------------------------------* args with normal parameter-----------------------

# # loop with args
# def multiply_num(*args):
#     multiply = 1

#     for i in args:
#         multiply *= i 
#     return(multiply)
# print(multiply_num(1,2,3))
# #output : 6



# loop with *args and normal function 
# def multiply_num(num,*args):
#     multiply = 1
#     print(num)       #output : 1
#     print (args)        #output : 2,3,1,5
#     for i in args:
#         multiply *= i 
#     return multiply
# print(multiply_num(1,2,3,1,5))
#output : 6






















#-----------------------------------*Args as argument-----------------------

# def multiply_num(*args):
#     multiply = 1
#     print (args)        #output : 2,3,1,5
#     for i in args:
#         multiply *= i 
#     return multiply
# num = [2,3,5]
# print(multiply_num(num))
# #output : [2, 3, 5]         # args cant work because we dont use args in argument
# print(multiply_num(*num))
# #output : 30























#-----------------------------------** Kwargs(kwargs = keyword arguments)-----------------------

# **kwargs(double star argument)
# kwargs (keyword argument)
# data gather dictionary


#kwargs as a parameter

def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    #output : <class 'dict'>

    for k,v in kwargs.items():
        print(f"{k} : {v}")
func(first_name = 'Jubayed' , last_name = 'Alam')

#output : {'first_name': 'Jubayed', 'last_name': 'Alam'}     #data store as a dictionary

# for output : first_name : Jubayed
               # last_name : Alam
