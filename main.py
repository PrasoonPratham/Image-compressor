import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
height , width = img.size 

img = img.resize((int(height*0.70),int(width*0.70)), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+"_compressed.jpg")