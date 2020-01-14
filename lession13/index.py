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
    
user_name =input ("Enter Your Name : ")
user_age  = int(input("Enter Your Age : "))
if(user_age >= 15 and (user_name[0] == 'a' or user_name[0] == 'A')):
    print ("You See The Movie")
else:
    print("You Don't See The Movie")