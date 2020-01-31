#----------------------------------Python Debugger-----------------------------


#we use first module today in python

#
import pdb                 #import pdb module
#module = > python file contains useful classes and function wrote by developer
# module use for debugging Program
#




#
# According to wikipedia = > debuggeding is the process of finding and resolving defects or problems withen a computer program that prevent currect operation of computer software or a system
#


#
#   why debugging
# 1. our program is not running and causing Unexpected Error
# 2. our programing is work fine but not working the same way we want
#



#
# Step for debugging
# 1. set trace 
# 2. execute code line by line 
#

pdb.set_trace()
name = input('Please Type Your Name .. ')
age  = int(input('Please Type Your Age .. '))
print(f'Hello {name} Your Age Is {age} ')

# age2 = age +5
# print(f'{name } you will be {age } in next 5 years ')


# when we start pdb then we need some commend for terminal
    # 1. l          # which line
    # 2. n          #next line
    # 3. c          #continue
