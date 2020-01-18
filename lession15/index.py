#------------------------- Python List Intro------------------------------ 
#rules for  making list 
#int
# numbers = [1,2,3,4,5]
# print(numbers) 
# #output :  [ 1,2,3,4]

# #string
# names = ['Python','Php','javaScript']
# print(names)
# #output : ['Python', 'Php', 'javaScript'] 

# #mix all datatype
# mixed = [1,2,'Python','javaScript',2.3,None]
# print(mixed)
# #output : [1, 2, 'Python', 'javaScript', 2.3, None]

# #access Element
# mixed = [1,2,'Python','javaScript']
# print(mixed[1])
# #output: 2


#-------------------------Add data to list (Append Method)------------------------------ 
#Append() Method 
# fruits = ['grapes','apple']
# fruits.append('Mango')
# print(fruits)
# #output: ['grapes', 'apple', 'Mango']

# #Real Life use Append Method
# fruits = []
# fruits.append('Mango')
# fruits.append('Grapes')
# fruits.append('Apple')
# fruits.append('Banana')
# print(fruits)
# #output : ['Mango', 'Grapes', 'Apple', 'Banana']

#-------------------------More methods to add data (insert() Method)------------------------------

#insert() Method
# fruits1 =['Mango','Banana']
# fruits1.insert(0,'Grapes')
# print(fruits1) 
#output: ['Grapes', 'Mango', 'Banana']

#-------------------------Concatenate Two List (+)------------------------------
# fruits1 =['Mango','Banana']
# fruits2 =['Grapes','Apple']
# fruits = fruits1+fruits2
# print(fruits)
#output : ['Mango', 'Banana', 'Grapes', 'Apple']

#-------------------------Extend() Method------------------------------ 
# fruits1 =['Mango','Banana']
# fruits2 =['Grapes','Apple']
# fruits1.extend(fruits2)
# print(fruits1)
#output : ['Mango', 'Banana', 'Grapes', 'Apple']

#-------------------------Append() Method------------------------------ 
#like Multi List
# fruits1 =['Mango','Banana']
# fruits2 =['Grapes','Apple']
# fruits1.append(fruits2)
# print(fruits1)
#output : ['Mango', 'Banana', ['Grapes', 'Apple']]



#-------------------------Delete data from list------------------------------ 

#delete last argument by pop() Method
# fruits = ['Mango','Banana','Grapes','Apple']
# fruits.pop()
# print(fruits)
# #output : ['Mango', 'Banana', 'Grapes']

# #delete position wise argument by pop() Method
# fruits = ['Mango','Banana','Grapes','Apple']
# fruits.pop(0)
# print(fruits)
# #output : ['Banana', 'Grapes', 'Apple']

# #delete position wise argument by del() Method
# fruits = ['Mango','Banana','Grapes','Apple']
# del fruits[0]
# print(fruits)
# #output : ['Banana', 'Grapes', 'Apple']


# #delete Unknown Variable argument by remove() Method
# fruits = ['Mango','Banana','Grapes','Apple']
# fruits.remove('Grapes')
# print(fruits)
# #output : ['Mango', 'Banana', 'Apple']


#-------------------------In keyword with list------------------------------ 

# fruits = ['Mango','Banana','Grapes','Apple']

# if 'Mango' in fruits:
#     print('Mango is Present')
# else:
#     print('Mango Not Present')
#output : Mango is Present

#-------------------------Count Method ------------------------------ 
# fruits = ['Mango','Banana','Grapes','Apple']
# print(fruits.count('Mango'))
#output : 1

#-------------------------Sort Method ------------------------------ 
# fruits = ['Mango','Banana','Grapes','Apple']
# numbers = [9,8,7,6,5,4,3,2,1]
# fruits.sort()
# numbers.sort()
# print(fruits)
# print(numbers)
#output : ['Apple', 'Banana', 'Grapes', 'Mango']
#output : [1, 2, 3, 4, 5, 6, 7, 8, 9]

#-------------------------sorted Function ------------------------------ 
# numbers = [9,8,7,6,5,4,3,2,1]
# print(sorted(numbers))
#output : [1, 2, 3, 4, 5, 6, 7, 8, 9]


#-------------------------Clear Method ------------------------------ 
# numbers = [9,8,7,6,5,4,3,2,1]
# numbers.clear()
# print(numbers)
#output : []


#-------------------------Copy Method ------------------------------ 
numbers = [9,8,7,6,5,4,3,2,1]
numbers_copy=numbers.copy()
print(numbers_copy)
#output : [9, 8, 7, 6, 5, 4, 3, 2, 1]