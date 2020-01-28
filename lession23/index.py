#------------------------------------Enumerate function-----------------------------  

#
# we use enumerate function with for loop to track position of our item in iterable
#
 


 #
 #How we can do this without enumerate function
 #

names = ['Jubayed','Alam','Sujon']
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
for position,name in enumerate(names):
    print(f"{position} ---- > {name}")
#output : 
# 0 ---- > Jubayed
# 1 ---- > Alam
# 2 ---- > Sujon