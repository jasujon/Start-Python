#-----------------------------( split() ) More input in one value---------------------------


#for single single input


# name = input("Enter Your Name")
# age  = input("Enter Your Age")

# print(name)
# print(age)


#for Multi Input


#----------------------for space ----------------
# name,age= input("Enter Your Name And Age ").split()
# print("Your Name is " + name)
# print("Your Age Is " + age)


#----------------------for , ----------------
name,age= input("Enter Your Name And Age ").split(",")
print("Your Name is " + name)
print("Your Age Is " + age)