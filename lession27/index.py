#-----------------------------intro and built in errors(all errors)----------------------------------

#
#built in errors
#exception , how to handle them
#raise your own errors , debugging etc
#




#
# syntex error
#

#not error 
# def func() :
#     print('Hello World')
# func()
#output : hello world


# error show 
# def func :
#     print('Hello World')
# func()
#output : SyntaxError: invalid syntax           #because we missing syntex in function ()


# error in variable
# name = 'Israk'*
# print(name)
#output : SyntaxError: invalid syntax







#
# Indentation error
#


#indentation means space error

#not error
# def func():
#     print('Hello Israk')
#     print('Hello Sohan')
# func()
#output Hello Israk , Hello Sohan


# with indentation error
# def func():
#     print('Hello Israk')
#    print('Hello Sohan')
# func()
#output : IndentationError: unindent does not match any outer indentation level







#
# Name error
#


# no name defined but we call the name

# no error
# name = 'Israk'
# print(name)
#output : Israk

# with name error
# name = 'Israk'
# print(name1)
#output : NameError: name 'name1' is not defined



#
# Type error
#

#no error
# name = 'Israk'
# print('5' + name)
#output : 5Israk

# with type error
# name = 'Israk'
# print(5 + name)
#output : TypeError: unsupported operand type(s) for +: 'int' and 'str'




#
# Index error
#

#no error
# list = [1,2,3]
# print(list[1])
#output : 2


#with index error

# list = [1,2,3]
# print(list[3])
#output : IndexError: list index out of range









#
# Value error
#

#no error
# s = '5'
# print(int(s))
#output: 5

#with value error
# s = 'abc'
# print(int(s))
#output : ValueError: invalid literal for int() with base 10: 'abc'















#
# Attribute error
#


# no exesting in python but we called
# l = [1,2,3]
# l.push(2)       # python has no push method
# print(l)
#output : AttributeError: 'list' object has no attribute 'push'











#
# Key error
#

# #no error
# d = {'name' : 'Israk'}
# print(d['name'])
# #output : Israk


#with key error
# d = {'name' : 'Israk'}
# print(d['age'])
#output : KeyError: 'age'






















#-----------------------------Raise errors----------------------------------

# def func(a,b):
#     return a+b
# # print(func(2,3))
# # #output : 5

# #if we pass string 
# print(func('5','5'))
# #output : 55       # but we want to get string



# def func(a,b):
#     if (type (a) is int ) and (type(b) is int):
#         return a+b
#     raise TypeError('Please give me number')
# # print(func(5 , 5))
# # #output : 10
# print(func('5','5'))
#output : TypeError: Please give me number




















#-----------------------------Try , Except : exception handling----------------------------------


# while True : 
#     try : 
#         age = int(input('Enter Your Age .. '))
#         break
#     except ValueError:
#         print('Invalid Input')

# if age < 10 :
#     print('You can\'t play play this game' )
# else:
#     print('You can play play this game' )
























#-----------------------------Else finally with try except----------------------------------

# while True :
#     try:
#         number = int(input('Enter A Number .. '))
#     except ValueError :
#         print('Please Type Integer .. ')
#     except :
#         print('Unexpected Error ..')
#     else:
#         print(f'User Input : {number}')
#         break
    





























#-----------------------------Custom Exception----------------------------------

# class NameToShortError(ValueError):
#     pass

# def validate (name):
#     if len(name) < 8 : 
#         raise NameToShortError('Name is Too Short')

# username = input('Enter Your Name ')
# validate(username)
# print(f'Hello {username}')