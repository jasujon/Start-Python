#-----------------------String Methods(Function & Method) ----------------- 


name = "Python"
#len() function
print(len(name))
#output   6


#lower() Method
name1 = "JUBAYED ALAM"
print(name1.lower()) 
#output  jubayed alam


#upper() Method
name2 = "jubayed alam"
print(name2.upper())
#output  JUBAYED ALAM

#title() method
name3 = "JUBAYED ALAM"
print(name3.title())
#output Jubayed Alam

#count() Method
name4 = "Jubayed Alam"
print(name4.count("a"))
#output   2


#--------------------------Strip Method $ Replace Method----------------------- 

lang = "        Python            "
dots ="............"
print(lang+dots)
#output :          Python            ............

#Remove Left Space
print(lang.lstrip() + dots)
#output: Python            ............

#Remove Right Space 
print(name.rstrip() + dots)
#output:   Python............

#Remove All Space
print(name.strip() + dots)
#output:Python............


####Replace Method
lang1 = "Pyt     hon"
print(lang1.replace(" " , ""))
#output: Python
