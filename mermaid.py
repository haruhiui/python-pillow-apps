
import os 
import random
from PIL import Image, ImageDraw 

def mermaid() -> str: 
    # find next number for file  
    pic_path = 'images/'
    out_path = 'output/'
    for _, _, fns in os.walk(pic_path): 
        pass 

    # get random fns 
    l0 = [fns[i] for i in random.sample(range(len(fns)), len(fns))] 
    # print(l0) 
    l1 = [] 
    for i in range(len(fns)): 
        if not l0[i].startswith('joint_mermaid'): 
            l1.append(l0[i]) 
        if len(l1) == 5: 
            break 
    print(l1) 
    l2 = ['joint_mermaid_%d.jpg' % i for i in range(1, 7)]
    images_name = [pic_path + l2[0]] 
    for i in range(0, 5): 
        images_name.append(pic_path + l1[i]) 
        images_name.append(pic_path + l2[i+1]) 
    # print(images_name) 

    # width = 500 and get heights for those files 
    images = [Image.open(f) for f in images_name] 
    images_width = [x.size[0] for x in images] 
    images_height = [x.size[1] for x in images] 
    width = 500 
    heights = [int(width / images_width[i] * images_height[i]) for i in range(0, len(images))]

    # resize images 
    new_images = [images[i].resize((width, heights[i]), Image.ANTIALIAS) for i in range(0, len(images))] 
    final_image = Image.new('RGB', (500, sum(heights))) 
    now_height = 0 
    for image in new_images: 
        final_image.paste(image, (0, now_height, 500, now_height + image.size[1])) 
        now_height += image.size[1] 
    final_image.save(out_path + 'mermaid.png', 'png') 
    return out_path + 'mermaid.png'

if __name__ == '__main__': 
    fn = mermaid() 
    print(fn) 