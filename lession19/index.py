#-------------------------What is list comprehension------------------------------

#List Comprehension Related With List
#List Comprehension Work Just sorted by Progranming Code


# #normal function for square
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)
# # output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# #List Comprehension for square
# square2 = [i**2 for i in range (1,11)]
# print(square2)
# # output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# #Negative Number Show Like -1 to -10 Function

# #normal function
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
# #output : [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


# #List Comprehension
# new_negative = [-i for i in range(1,11)]
# print(new_negative)
# #output : [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]















#---------------------------------List Comprehension with if statement-------------------------------

# numbers = list(range(1,11))
# # print(numbers)
# #output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# #normal function
# num = []
# for i in numbers : 
#     if i%2 == 0 :
#         num.append(i)
# print(num)
#output : [2, 4, 6, 8, 10]

#List Comprehension
even_num = [i for i in range(1,11) if i%2 == 0]
print(even_num)
#output : [2, 4, 6, 8, 10]
