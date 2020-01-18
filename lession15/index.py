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
fruits1 =['Mango','Banana']
fruits1.insert(0,'Grapes')
print(fruits1) 
#output: ['Grapes', 'Mango', 'Banana']