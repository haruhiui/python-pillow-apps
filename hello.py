
from PIL import Image, ImageFilter, ImageChops 
import numpy as np 

img: Image.Image = Image.open('images/001.png') 

# thumbnail 
# w, h = img.size 
# print(w, h, w//2, h//2)  
# img.thumbnail((w//2, h//2)) 
# img.save('images/001_thumbnail.png', 'png') 

# blur 
# img_blur = img.filter(ImageFilter.BLUR) 
# img_blur.save('images/001_blur.png', 'png') 

# to gray 
# img_gray = img.convert('L') 
# img_gray.save('images/001_gray.png', 'png') 

# image invert  
# img_invert = ImageChops.invert(img_gray) 
# img_invert.save('images/001_invert.png', 'png') 

# np 
# img_np = np.array(img_gray) 
# for h in range(img_gray.size[1]): 
#     for w in range(img_gray.size[0]): 
#         print(img_np[h, w]) 
#     break 

img_array = np.array(img) 
img_new = Image.fromarray(np.uint8(img_array)) 
img_new.save('images/001_new.png', 'png')  
