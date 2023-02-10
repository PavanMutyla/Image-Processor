from PIL import Image,ImageFilter,ImageEnhance
img = Image.open('C:\\Users\\PAVAN\\Desktop\\image pro\\image\\bulbasaur.jpg')
fil_img = img.filter(ImageFilter.SHARPEN)
fil_img.save('blur.png','png')
"""print(img.format)
print(img.mode)"""
f_img = img.convert('L')
f_img.save('Grey.png','png')
rot = f_img.rotate(180)
rot.save('Rot.png','png')

resize = img.resize((100,100))
resize.save('rea.png','png')

box = [0,0,400,400]
crop = img.crop(box)
crop.save('crop.png','png')

# for brigthness
#image brightness enhancer
enhancer = ImageEnhance.Brightness(img)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 0.5 #darkens the image
im_output = enhancer.enhance(factor)
im_output.save('darkened-image.png')

factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.save('brightened-image.png')
