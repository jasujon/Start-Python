#-----------------------------Functions Intro & Function Exm --------------------------------- 

#add two number
# def add_two(a,b):
#     return a+b
# total = add_two(5,5)
# print(total)

#output 10

#get input user and print total

# def add_two(num1,num2):
#     return num1+num2

# a = int(input("Enter First Number : ")) #10
# b = int(input("Enter Second Number : ")) #10

# total = a+b
# print(total)
#output : 20


#get user first Name

# def user_name(a,b):
#     return a + b
# firstName = input("Enter Your First Name : ")
# lastName  = input("Enter Your Last Name : ")
# print(user_name(firstName,lastName))


#-----------------------------Show String Last Char --------------------------------- 

# def last_char(name):
#     return name[-1]
# print(last_char("Sujon"))
#output : n


#-----------------------------Odd or Even Function --------------------------------- 

# def odd_even(num):
#     if num%2 == 0:
#         print("This is Even Number ")
#     else:
#         print("This is Odd Number")

# print(odd_even(7))
# #output : This is Odd Number
# print(odd_even(10))
# #output : This is Even Number

#-----------------------------Define greatest By Function--------------------------------- 

def greatest(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(20,30,10))
#output 30