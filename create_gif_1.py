
from PIL import Image 
import numpy as np 
import imageio 


def create_gif_1(image_names, gif_name, duration=1.0): 
    """
    Not good enough when there are different size images.
    """ 
    frames = [] 
    for fn in image_names: 
        frames.append(imageio.imread(fn)) 

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration) 
    

def create_gif_2(image_names, gif_name, duration=1.0): 
    """
    Not good enough too. 
    """ 
    frames = [] 
    for fn in image_names: 
        frames.append(Image.open(fn)) 
    # im = Image.new('RGBA', (2000, 2000)) 
    frames[0].save(gif_name, save_all=True, append_images=frames, loop=1, duration=duration) 


if __name__ == '__main__': 
    image_names = ['images/201.jpg', 'images/101.png', 'images/102.png', 'images/103.png'] 
    gif_name = 'output/gif.gif' 
    create_gif_1(image_names, gif_name, 1) 
