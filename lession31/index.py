#----------------------------Edit IMAGES using PYTHON--------------------------------


#
# For image we use pillow library
#


#
# For install pillow library we need this command
# pip install Pillow
# pit install complite than we need to import 
# 
#


#from PIL import Image

# we need os for loop
#

# 
# change image extention(like jpg to png)
#


#first we need to open image
#img1 = Image.open('image1.jpg')
# img1.save('image1.png')
#output : image1 change to image1.png

# img1.show()
#output : show the image


#
# For image resize
#

# max_size = (250,250)
# img1.thumbnail(max_size)
# img1.save('newimage.png')



#
# all image extension change
#

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         #for open image
#         img1 = Image.open(item)
#         #for get image name
#         filename,extention = os.path.splitext(item)
#         img1.save(f'{filename}.png')







#--------------------------------------------Sharpness----------------------------------------------

# if we need to sharpness in our image than we nee to import ImageEnhance with Image


from PIL import Image , ImageEnhance

img1 = Image.open('image1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(0).save('editimage.png')



# 0 = blurry
# 1 = original image
# 3 = image with increased sharpness




#--------------------------------------------color----------------------------------------------

# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save('editimage.png')


# 0 = Black And White 
# 1 = original image
# 3 = image with increased color



#--------------------------------------------Brightness----------------------------------------------

# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(0).save('editimage.png')


# 0 = Black
# 1 = original image
# 3 = image with increased color


#--------------------------------------------Contrast----------------------------------------------


enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(2).save('editimage.png')


# 0 = Black
# 1 = original image
# 3 = image with increased Contrast







