#------------------------------Tuples Intro--------------------------- 

#Tuples Data Structure
#Tuples Store Any Datatype (like List)
#Most important tuples are immutable, once tuples is created you cant update 

# example = ('one','two','three')     #this is a tuples
#now you cant no append , no insert , no pop , no remove
#tuples are faster than list


#Tuples can  use Method ()
#count 
#index
#len function
#slicing 


#------------------------------Looping in Tuples---------------------------
# mixed = (2,45,6,2.9)

# for num in mixed : 
#     print(num)

#------------------------------Tuples With One Element--------------------------- 

# #num = (1) # its not a tuples
# num = (1,) # tuples
# #output <class 'tuple'>
# print(type(num))
# #output <class 'int'>


#------------------------------Tuples Without Parenthesis--------------------------- 
# lang = 'Python','javaScript','Php','Laravel'
# # print(type(lang))
# #output : <class 'tuple'>
# print(lang)
# #output : ('Python', 'javaScript', 'Php', 'Laravel')


#------------------------------Tuples Unpacking---------------------------
lang = ('Python','javaScript','Php','Laravel')
lang1,lang2,lang3,lang4 =(lang)
print(lang1)
#output : Python