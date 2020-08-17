# python-pillow-apps 

hello.py: 几个简单的pillow使用方法。

identify_code.py：使用pillow生成一个验证码图片。

image_merger.py：利用png的透明特性，生成缩略图和大图看起来不相同的图片。

mermaid.py：一个生成setu版美人鱼名场景的程序。（lsp了）

create_gif_1.py：生成gif图片的一些尝试

create_gif.py：生成gif图片，经过优化，可以根据原图片列表的尺寸不同来调整参数，mode的参数：
* fit-min: 将图片拉伸到最长的边对齐
* fit-max: 将图片拉伸到最小的边对齐
* fill: 不将图片进行拉伸
  
同时可以调整size，不调整时分别寻找原图片中最大的长和宽作为产生gif的长和宽。

