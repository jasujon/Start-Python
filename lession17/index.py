# #------------------------Intro to dictionaries--------------------- 
# #intro dictionaries
# #Dictionaries is a Unordered collections of Data
# # You Can Store Any DataType  (string,int,boolean,float etc)

# #create Dictionaries (One) 
# user = {'name' : 'Sultan','age' : 10}
# print(user)
# #output : {'name': 'Sultan', 'age': 10}
# print(type(user))
# #output: <class 'dict'>

# #create Dictionaries (Two)
# user1 = dict(name = 'Sultan' , age = 10)
# print(user1) 
# #output : {'name': 'Sultan', 'age': 10}
# print(type(user1))
# #output: <class 'dict'>


# ##Dictionaries Indexing 
# # print(user1[0])
# ##output : TypeError (Error)
# print(user['name'])
# #output : sultan


# # 
# user_info = {
#     'name' : 'Sultan',
#     'age'  :10,
#     'fav_movies' : ['Motu-Patlu','Gopal Bar'],
#     'fav_lang'  : ['Python','javaScript']

# }
# print(user_info)
# #output : {'name': 'Sultan', 'age': 10, 'fav_movies': ['Motu-Patlu', 'Gopal Bar'], 'fav_lang': ['Python', 'javaScript']}
# print(user_info['fav_movies'])
# #output : ['Motu-Patlu', 'Gopal Bar']
# print(type(user_info))
# #output: <class 'dict'>




# #Data Store
# user2 ={}
# user2['name'] = 'Sultan'
# user2['age']  =  10
# print(user2)
# #output : {'name': 'Sultan', 'age': 10}






#---------------Looping and In Keyword in dictionary--------------------- 

# #in Keyword (if key exist in dictionary or not exist )

# user_info = {
#     'name' : 'Sultan',
#     'age'  :10,
#     'fav_movies' : ['Motu-Patlu','Gopal Bar'],
#     'fav_lang'  : ['Python','javaScript']
# }
# if 'name' in user_info :        # ii just check key name
#     print('present')
# else:
#     print('not Present')
# #output : present

# #check if value exist in Dictionary
# if 'Sultan' in user_info.values() :        # ii just check key name
#     print('present')
# else:
#     print('not Present')
# #output : present


# # looping in Dictionary 
# for i in user_info.values():
#     print(i)


# #get all keys name 
# user_info_keys = user_info.keys()
# print(user_info_keys)
# #output : dict_keys(['name', 'age', 'fav_movies', 'fav_lang'])
# print(type(user_info_keys))
# #<class 'dict_keys'>






#--------------- Item Method ---------------------
# user_info = {
#     'name' : 'Sultan',
#     'age'  :10,
#     'fav_movies' : ['Motu-Patlu','Gopal Bar'],
#     'fav_lang'  : ['Python','javaScript']
# }

# user_items = user_info.items()
# print(user_items)
# #output : dict_items([('name', 'Sultan'), ('age', 10), ('fav_movies', ['Motu-Patlu', 'Gopal Bar']), ('fav_lang', ['Python', 'javaScript'])])
# print(type(user_items))
# #output : <class 'dict_items'>






#--------------- Add and delete data from dictionaries --------------------- 
# user_info = {
#     'name' : 'Sultan',
#     'fav_lang'  : ['Python','javaScript']
# }

# # add data one 
# user_info['fav_songs'] = ['song1','song2']
# print(user_info)
# #output ; {'name': 'Sultan', 'fav_lang': ['Python', 'javaScript'], 'fav_songs': ['song1', 'song2']}

# #Pop Method 
# deleted_user_info = user_info.pop('fav_lang')
# print(user_info)
# #output : {'name': 'Sultan', 'fav_songs': ['song1', 'song2']}







#-------------------------Update Dictionary-------------------------------- 
 
# user_info = {
#     'name' : 'Sultan',
#     'fav_lang'  : ['Python','javaScript']
# }

# #print(user_info)
# #output : {'name': 'Sultan', 'fav_lang': ['Python', 'javaScript']}

# more_info = {'name' : 'Jubayed' ,'Age' : 10}
# #print(more_info)
# #output : {'name': 'Jubayed', 'Age': 10}

# user_info.update(more_info)
# print(user_info)
# #output : {'name': 'Jubayed', 'fav_lang': ['Python', 'javaScript'], 'Age': 10}







#-------------------------fromkeys Method--------------------------------  

# #fromkeys method 
# #fromkeys manes same value
# #d = {'name' : 'unknown','age' : 'unknown' , 'language' : 'unknown'}

# d = dict.fromkeys(['name','school','program'],'unknown')
# print(d)
# #output : {'name': 'unknown', 'school': 'unknown', 'program': 'unknown'} 





#-------------------------get Method-------------------------------- 

# d = {'name' : 'Jubayed','age' : 'unknown' , 'language' : 'unknown'}
# # print(d['name'])
# #output : Jubayed

# #print(d['names'])
# #output : error (keyError)

# # get method work error hanglaning
# print(d.get('name'))
# #output : Jubayed       #(No Error)
# print(d.get('names'))
# #output : None          # this time no error pace because we use get method







#-------------------------Word Counter Dictionary-------------------

def word_count (s):
    count = {}
    for char in s : 
        count[char] = s.count(char)
    return count

print(word_count('Sultan Alam'))
#output :  {'S': 1, 'u': 1, 'l': 2, 't': 1, 'a': 2, 'n': 1, ' ': 1, 'A': 1, 'm': 1}