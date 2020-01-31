#-----------------------------------Read Text Files - Python-----------------------------

#readfile
#open function
#read method
#seek method
#tell method
#readline method
#close method



#open function
# f = open('test.txt')
# # print(f)
# #output: <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>

# #tell method                #for check courser position
# print(f'Courser Position {f.tell()}')
# #output : Courser Position 0



# #read function
# print(f.read())
# #output : Hello World


# #close method
# f.close()           #for close file


# #tell method                #for check courser position
# print(f'Courser Position {f.tell()}')
# #output : Courser Position 11



#seek method use for change courser position        #seek()
#readline use for show line by line list ....       #line()








































#-----------------------------------File I/O : Write to file-----------------------------

#for read
# with open('test.txt', 'r') as f :
#     data= f.read()
#     print(data)
#output : Hello World



#write to file we can use  ( w,a,r+)

with open('test1.txt', 'w') as f :
    f.write('Hello')
#output : Hello World

### w create new text file and insert him ' ';