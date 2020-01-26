#-----------------------------Dictionary Comprehension -----------------------------


#square = {1:2,2:4,4:5}    # 1:2 => said key and value


#comprehension
square = {num:num **2 for num in range (1,11)}
print(square)
#output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



#for loop
for k,v in square.items():
    print(f"{k} : {v}")
#output : 
# 1 : 1    
# 2 : 4    
# 3 : 9    
# 4 : 16   
# 5 : 25   
# 6 : 36   
# 7 : 49   
# 8 : 64   
# 9 : 81   
# 10 : 100 




#string count 

name = "Sujon"
word_count = {char:name.count(char) for char in name}
print(word_count)
#output : {'S': 1, 'u': 1, 'j': 1, 'o': 1, 'n': 1}
