#----------------------------------------OS Module python(file create,del,edit)--------------------------

import os

#print(os.getcwd())          # for get working location
#output : C:\Users\sohan\Desktop\start-python\lession30


#os.mkdir('movies')          # for create holder this holder location

#open('file.txt','a').close()    #for create file this holder location

# print(os.path.exists('movies'))
#output : True
# if os.path.exists('movies'):
#     print('Already Exist')
# else:
#     os.mkdir('movies')


print(os.listdir())     #for show all file this holder location
output : ['file.txt', 'index.py', 'movies']

