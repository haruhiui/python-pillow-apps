
from PIL import Image 
import imageio 

image_path = 'images/' 

def create_gif_1(image_names, gif_name, duration = 1.0): 
    """
    Not good enough when there are different size images.
    """ 
    frames = [] 
    for fn in image_names: 
        frames.append(imageio.imread(fn)) 

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration) 
    

if __name__ == '__main__': 
    image_names = ['images/004.jpg', 'images/001.png', 'images/002.png', 'images/003.png'] 
    gif_name = 'output/gif.gif' 
    create_gif_1(image_names, gif_name, 0.5) 
