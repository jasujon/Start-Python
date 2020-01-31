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
d = {'name' : 'Israk'}
print(d['age'])
#output : KeyError: 'age'