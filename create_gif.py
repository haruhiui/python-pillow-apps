
from PIL import Image 
from functools import reduce 
import numpy as np 
import imageio 
import nonebot 

def create_gif(image_names: list, gif_name: str, size: tuple = None, 
    duration: float=1.0, mode: str='fit-min', fill_color: tuple = (0, 0, 0)): 
    # open images 
    frames = [] 
    for fn in image_names: 
        frames.append(Image.open(fn).convert('RGB')) 
    # extend images 
    if size == None: 
        size = [0, 0]
        size[0] = max([frame.size[0] for frame in frames])
        size[1] = max([frame.size[1] for frame in frames])
    frames = [extend_image(frame, size, mode=mode, fill_color=fill_color) for frame in frames] 
    # convert into np.array to use imageio 
    frames = map(np.array, frames) 
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration) 
    return gif_name 
    

def extend_image(image: Image.Image, size: tuple, mode: str = 'fit-min', 
    fill_color: tuple = (0, 0, 0)) -> Image.Image: 
    """
    Only RGB was supported, other will be converted into RGB, return result too. 
    :return: extended image 
    """
    # 
    if mode not in ['fit-min', 'fit-max', 'fill']: 
        raise ValueError('unknown mode') 
    # resize image 
    extend_size = get_extend_size(image.size, size, mode) 
    image = image.resize(extend_size, Image.ANTIALIAS).convert('RGB')
    # create extended image 
    image_array = np.array(image) 
    new_image_array = np.zeros((size[1], size[0], 3)) 
    start_x, end_x = int((size[1] - extend_size[1]) / 2), int((size[1] + extend_size[1]) / 2) 
    start_y, end_y = int((size[0] - extend_size[0]) / 2), int((size[0] + extend_size[0]) / 2) 
    # 
    for i in range(size[1]): 
        for j in range(size[0]): 
            if i in range(start_x, end_x) and j in range(start_y, end_y): 
                new_image_array[i, j] = image_array[i - start_x, j - start_y] 
            else: 
                new_image_array[i, j] = fill_color 

    new_image = Image.fromarray(np.uint8(new_image_array)) 
    return new_image 


def get_extend_size(oldsize, newsize, mode = 'fit-min'): 
    """
    :return: suitable resize tuple  
    """
    scale_x, scale_y = oldsize[0] / newsize[0], oldsize[1] / newsize[1] 
    width, height = newsize 
    if mode == 'fit-min': 
        if scale_x < scale_y: 
            width = int(oldsize[0] / scale_y) 
        else: 
            height = int(oldsize[1] / scale_x) 
    elif mode == 'fit-max': 
        if scale_x > scale_y: 
            width = int(oldsize[0] / scale_y) 
        else: 
            height = int(oldsize[1] / scale_x) 
    elif mode == 'fill': 
        width, height = oldsize  
    else: 
        raise ValueError('unknown mode') 
    return (width, height) 


def test(): 
    # print(get_extend_size((300, 150), (200, 400), 'fill')) 

    # im = Image.open('images/101.png') 
    # new_im = extend_image(im, (1500, 1500), 'fit-min') 
    # new_im.save('temp.jpg') 

    image_names = ['images/101.png', 'images/102.png', 'images/201.jpg'] 
    gif_name = 'temp.gif'
    create_gif(image_names, gif_name, duration=0.5, mode='fill') 
    

if __name__ == '__main__': 
    test() 