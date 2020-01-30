#-----------------------------Intro to generators-------------------------------------

#generators 
#generators  are interators


#
# We are many hear iterator and iterable in python 
#

#iterable : 

l = [ 1,2,3 ]       # iterable
# for i in l :
#     print(i)
# #output : 1,2,3

#
# But this list first convert iterator than show output 
#

i = iter(l)
print(next(i))
#output : 1
print(next(i))
#output : 2
print(next(i))
#output : 3
# print(next(i))
#output : Error # because we have three value

# next(l)               # next function just use in iterator  but we can't use iterable
#output : Error 








#iterator :
#map(lambda a: a**2 , l )        #iterator
#
# In python map function is remain in iterator from first 
#
# print(map(lambda a: a**2 , l ) )
# output : <map object at 0x003AA250>

for num in map(lambda a: a**2 ,l):
    print(num)
#output : 1,4,9









#generators

# l = [ 1,2,3,54,6,7]

# memory --------> [---------------------------------------------]      # list  # its show all list in one line .. for this reason big memory for store all data

#memory-------->(1)         => its show just one value in one time so its need small memory  . if we need to show second number than generators remove first number and show second number ... 