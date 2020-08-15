
from PIL import Image, ImageDraw, ImageFont, ImageFilter 
import random 

def randChar(): 
    return chr(random.randint(65, 90)) 

def randColor(): 
    return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255)) 

def identify_code(): 
    width = 60 * 4 
    height = 60 
    img = Image.new('RGB', (width, height), (255, 255, 255)) 
    font = ImageFont.truetype('arial.ttf', 36) 
    draw = ImageDraw.Draw(img)

    for x in range(width): 
        for y in range(height): 
            draw.point((x, y), fill=randColor()) 

    for t in range(4): 
        draw.text((60 * t + 10, 10), randChar(), font=font, fill=randColor()) 

    img = img.filter(ImageFilter.BLUR) 
    img.save('output/identify_code.jpg', 'jpeg') 

if __name__ == '__main__': 
    identify_code() 