##-----------------------If StateMent-------------------- 

# age = input("Enter Your Age : ")
# age = int(age)
# if age >= 14 :
#     #print("Line a ")
#     print("You Are Above 14")

##-----------------------Pass StateMent--------------------  

# x = 18
# if x>18:
#     pass
# #output null

##-----------------------if else StateMent-------------------- 

# age = int(input("Enter Your Age : "))
# if age >= 10:
#     print("You Can Play The Game")
# else:
#     print("You Can't Play The Game")


##-----------------------Nested If-else StateMent-------------------- 

# warning_number = 50
# user_input = input("Guess A Number b/w 1 To 100 : ")
# user_input = int(user_input)     #string value convert integer

# if(warning_number == user_input):
#     print("You Win !!!!!")
# else:
#     if(user_input < warning_number):
#         print("Too Low")
#     else:
#         print("Too High")


##-----------------------And, Or Operator StateMent-------------------- 

## And StateMent
# name = "python"
# age  = 20
# if name == "python" and age == 20 :
#     print("Condition True")
# else:
#     print("Condition False")

# ##Or StateMent
# if name == "python" or age == 20 :
#     print("Condition True")
# else:
#     print("Condition False")
    
# user_name =input ("Enter Your Name : ")
# user_age  = int(input("Enter Your Age : "))
# if(user_age >= 15 and (user_name[0] == 'a' or user_name[0] == 'A')):
#     print ("You See The Movie")
# else:
#     print("You Don't See The Movie")


##-----------------------If-elif-else statement--------------------  

# age = input("Please Type Your Age : ")
# age = int(age)

# if 0<age <=3:
#     print("Ticket Price : Free ")
# elif 3<age<=10:
#     print("Ticket Price : 150 TK ")
# elif 10< age <=60:
#     print("Ticket Price : 250 TK")
# else:
#     print("Ticket Price : 200 TK")


##-----------------------in keyword--------------------  
# name = "Jubayed Alam"
# if 'a' in name :
#     print("A Is Present in Name")
# else:
#     print("Not Present")

##-----------------------While Loop--------------------  
# i = 1 
# while i<= 10 :
#     print("Hello World")
#     i = i+1

##-----------------------Sum of Numbers Program using while loop--------------------  

# total = 0
# i = 1
# while i<=10 :
#     total = total + i
#     i = i + 1
# print(total)
# #output 55

##-----------------------Infinite loop-------------------- 

# i = 0
# while i<=10:
#     print("Hello World")
#     # forget end by i = i+1
# while True :
#     print("Hello World")
##

##-----------------------For loop-------------------- 

# for i in range(10):
#     print("Hello World")

##sum from 1 to 10
# total = 0
# for i in range (1,10):
#     total += i
# print(total)
#output : 45

##-----------------------Break and Continue keyword-------------------- 

#break keyword
for i in range(1,11):
    if i == 5 :
        break
    print(i)

##Continue keyword
#print 1 to 10 but not 5

for i in range(1,11):
    if i==5:
        continue
    print(i)
#output :  1,2,3,4,6,7,8,9,10