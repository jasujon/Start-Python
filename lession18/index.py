#--------------------Intro to Sets------------------ 


#set data type
#set means unordered collection of unique items

#create set
# s = {1,2,3,4,3,5}
# print(s)
#output: {1, 2, 3, 4, 5}   # no duplicate show like (3 remove)
# print(type(s)) 
#output : <class 'set'>


# set can store any datatype value without List and Dictionary
# n = { 1,2,4.3,'string'}
# print(n)
#output : {1, 2, 'string', 4.3}



# N = {1,2,3,4,5,6,7,8,1,3,5,74,6,7,8}
# # s = set(N)
# # print(s)
# #output : {1, 2, 3, 4, 5, 6, 7, 8, 74}


### for convert list
# s= list(set(N))
# print(s)
#output : [1, 2, 3, 4, 5, 6, 7, 8, 74]



#--------------some method for set-----------------------

n = {1,2,3}
#add method 
# n.add(4)
# print(n)
#output: {1, 2, 3, 4}


#remove method
# n.remove(3)
# print(n)
#output : {1, 2}


# discard method 
# n.remove(3)
# print(n)
#output: {1, 2}



# try to remove unknown value
# n.remove(5)
# print(n)
#output : KeyError 



n.discard(5)
print(n)
#output : {1, 2, 3}