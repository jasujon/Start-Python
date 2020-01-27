#------------------------------------Intro to *args / *operator-----------------------------


#  *operator
#  *args


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
def all_total(*args):
    total = 0
    for num in args :
        total  += num
    return total
print(all_total(1,2,3))
#output : 6