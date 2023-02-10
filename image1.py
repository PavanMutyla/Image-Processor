from PIL import Image
img = Image.open('C:\\Users\\PAVAN\\Desktop\\image pro\\image\\astro.jpg')
n_img = img.resize((400,400))
n_img.save('new.png','png')
# thumbnail
img.thumbnail((232,222)) # thumbnail doesnot return anytthing 
img.save('thumb.png','png')

print(img.size)