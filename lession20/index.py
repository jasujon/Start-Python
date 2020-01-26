#-----------------------------Dictionary Comprehension -----------------------------


#square = {1:2,2:4,4:5}    # 1:2 => said key and value


# #comprehension
# square = {num:num **2 for num in range (1,11)}
# print(square)
# #output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



# #for loop
# for k,v in square.items():
#     print(f"{k} : {v}")
# #output : 
# # 1 : 1    
# # 2 : 4    
# # 3 : 9    
# # 4 : 16   
# # 5 : 25   
# # 6 : 36   
# # 7 : 49   
# # 8 : 64   
# # 9 : 81   
# # 10 : 100 




# #string count 

# name = "Sujon"
# word_count = {char:name.count(char) for char in name}
# print(word_count)
# #output : {'S': 1, 'u': 1, 'j': 1, 'o': 1, 'n': 1}


















#-----------------------------Dictionary comprehension with if else-----------------------------

# d = {1 : 'odd' , 2 : 'even'}

# odd_even = {i:('even' if i%2 == 0 else 'odd') for i in range (1,11)}
# print(odd_even)

#output : {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}





















#-----------------------------Sets comprehension-----------------------------

#random order change

names = ['Sujon',"Jusbayed","Alam"]
first = {name[0] for name in names}
print(first)

#output 1st time  = {'J', 'S', 'A'}
# output 2nd time = {'A', 'J', 'S'}