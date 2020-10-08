from PIL import Image, ImageFilter, ImageOps

cm_pixel = 118
size = 1157
image_number = 0
image_type_input = None
blur = 6
frame = False
background = Image.open("frame.png")
background2 = Image.open("frame.png") 

def proportional_value(size_proportional, size_resize, size_new ):
   return int((size_proportional * size_new) / size_resize)

#redimenciona con un tamaño maximo
def resize(x,y, size_max):
   img_new = None
   background = None
   img_size = None
   background_size = (size_max,size_max)
   if x > y:
      size = (size_max, proportional_value(y, x, size_max))
      background_size = (proportional_value(x, y, size_max), size_max)
   elif y > x:
      size = (proportional_value(x, y, size_max), size_max)
      background_size = (size_max, proportional_value(y, x, size_max))
   else:
      size = (size_max, size_max)

   background = img.resize(background_size)
   background = background.filter(ImageFilter.GaussianBlur(blur))
   img_new = img.resize(size, Image.ANTIALIAS)
   x_center = int((background.size[0]-img_new.size[0])/2)
   y_center = int((background.size[1]-img_new.size[1])/2)
   background.paste(img_new,(x_center,y_center))
   x_cut = int((background.size[0]-size_max)/2)
   y_cut = int((background.size[1]-size_max)/2) 
   img_new = ImageOps.crop(background, (x_cut, y_cut, x_cut, y_cut ))
   return img_new

#verificador de que sea jpg o png
def image_input_type():
   try:
      text = "1. jpg\n"
      text += "2. png\n"
      text += "Ingrese: "
      img_type = int(input(text))
   except:
      print("\nValor incorecto por favor elija un numero\n")
      img_type = image_input_type()
   finally:
      if img_type == 1:
         return "JPG"
      elif img_type == 2:
         return "PNG"
      elif type(img_type) == str:
         return img_type
      else:
         print("\nValor incorecto por favor elija un numero valido\n")
         img_type = image_input_type()
         return img_type



print("\nQue tipo de fromatos son las fotos a ingresar:")
image_type_input = image_input_type()

print("\nllevara marco?\n0. no\n1. se")
frame = False if int(input("Ingrese valor: ")) == 0 else True

print("\nEl tamaño total de la imagen (ejemplo: si va a ser de 10x10 ponga 10)")
size = cm_pixel * int(input("Ingrese valor: "))

image_number = int(input("Ingrese la cantidad de imagenes: "))

if frame:
   background = Image.new("RGBA",(size,size),"white")
   background2 =  background2.resize((size,size))
   size -= int((cm_pixel*2)*(int(size/118))/10) # realizo esta cuenta para que su reduccion sea proporcional realizando reiglade 3 simples

for i in range(image_number):
   name = str(i+1)+"."+ image_type_input.lower()
   img = Image.open(name)
   img_size = img.size
   img = resize(img_size[0], img_size[1],size)
   if frame:
      x_center = int((background.size[0]-size)/2)
      y_center = int(((background.size[1]-size)/2)-int((cm_pixel/2)*(int(size/118))/10))
      background.paste(img,(x_center,y_center))
      background.paste(background2,(0,0),background2)
      background.save("new_" + str(name)+".png", "PNG")
   else:
      img.save("new_" + str(name)+".png", "PNG")
