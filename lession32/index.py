#------------------------------First Project using python (GUI next )-----------------------------

#
#this project we create holder programmatically for videos we create video holder , for audio we create audio holder, for documents we create documents holder 
# 


import os,shutil


# print(os.getcwd())
# You can write every single externsions inside tuples

dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav'),
    'video_extensions' : ('.mp4','.mkv','.mpeg'),
    'documents_extensions' : ('.doc','.pdf','.txt'),
}




# audio_extensions = ('.mp3','.m4a','.wav')
# video_extensions = ('.mp4','.mkv','.mpeg')
# documents_extensions = ('.doc','.pdf','.txt')


#first we need holder path .. we get holder location in user .. 
folderpath = input('Enter Holder Path : ')

def file_finder(folder_path,file_extentions):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files.append(file)
    return files

# print(file_finder(folderpath,video_extensions))
#output : ['western_bluebird_bird_perched_tree_684.mp4']


#we use items function when we need loop in dict
for extention_type,extention_tuple in dict_extensions.items():
    # print('Calling File Finder ')
    # print(file_finder(folderpath,extention_tuple))

    # create folder name
    folder_name = extention_type.split('_')[0] + 'False'
    # find folder path
    folder_path = os.path.join(folderpath,folder_name)
    #create holder
    os.mkdir(folder_path)

    for item in file_finder(folderpath,extention_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)





