#------------------------Intro to dictionaries--------------------- 
#intro dictionaries
#Dictionaries is a Unordered collections of Data
# You Can Store Any DataType  (string,int,boolean,float etc)

#create Dictionaries (One) 
user = {'name' : 'Sultan','age' : 10}
print(user)
#output : {'name': 'Sultan', 'age': 10}
print(type(user))
#output: <class 'dict'>

#create Dictionaries (Two)
user1 = dict(name = 'Sultan' , age = 10)
print(user1) 
#output : {'name': 'Sultan', 'age': 10}
print(type(user1))
#output: <class 'dict'>


##Dictionaries Indexing 
# print(user1[0])
##output : TypeError (Error)
print(user['name'])
#output : sultan


# 
user_info = {
    'name' : 'Sultan',
    'age'  :10,
    'fav_movies' : ['Motu-Patlu','Gopal Bar'],
    'fav_lang'  : ['Python','javaScript']

}
print(user_info)
#output : {'name': 'Sultan', 'age': 10, 'fav_movies': ['Motu-Patlu', 'Gopal Bar'], 'fav_lang': ['Python', 'javaScript']}
print(user_info['fav_movies'])
#output : ['Motu-Patlu', 'Gopal Bar']
print(type(user_info))
#output: <class 'dict'>




#Data Store
user2 ={}
user2['name'] = 'Sultan'
user2['age']  =  10
print(user2)
#output : {'name': 'Sultan', 'age': 10}
