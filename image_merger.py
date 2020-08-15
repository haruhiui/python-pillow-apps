
"""
将任意两张图片合成，达到显示的缩略图和大图不一样的效果
white: 白色背景下显示的图片，白色透明
black：黑色背景下显示的图片，黑色透明
电脑上black是缩略图，white是大图，QQ上正好相反（大概）
"""

from PIL import Image 
import numpy as np 

def merge(white: str, black: str) -> str: 
    ret = '' 
    white: Image.Image = Image.open(white).convert('L') 
    black: Image.Image = Image.open(black).convert('L') 
    black = black.resize((white.size[0], int(white.size[0] / black.size[0] * black.size[1])), Image.ANTIALIAS) 

    # pad the lower 
    w, h1, h2 = white.size[0], white.size[1], black.size[1] 
    if h1 < h2: 
        white1 = Image.new('L', (w, h2), 255)
        white1.paste(white, (0, int((h2-h1)/2), w, int((h2+h1)/2)))
        white = white1 
    else: 
        black1 = Image.new('L', (w, h1), 0)
        black1.paste(black, (0, int((h1-h2)/2), w, int((h2+h2)/2)))
        black = black1 

    white_array = np.array(white) 
    black_array = np.array(black) 

    # merge 
    output_array = np.zeros((max(h1, h2), w, 4)) 
    print(white.size, black.size) 
    print(white_array.shape, black_array.shape, output_array.shape) 
    for i in range(max(h1, h2)): 
        for j in range(w):  
            gray = int(white_array[i, j] * 0.5 + black_array[i, j] * 0.5) 
            alpha = int((255 - white_array[i, j]) * 0.5 + black_array[i, j] * 0.5) 
            output_array[i, j] = (gray, gray, gray, alpha) 
    output = Image.fromarray(np.uint8(output_array))
    output.save('output/merge.png', 'png') 
    return 'output/merge.png'

if __name__ == '__main__': 
    im = merge(white='images/001.png', black='images/002.png') 
    # Image.open(im).show() 