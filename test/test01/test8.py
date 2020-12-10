from pyexiv2 import Image

img = Image('WechatIMG3.jpeg')
data = img.read_exif()
data=str(data).replace('.',' ')
with open('1.txt',mode='w',encoding='utf-8') as f:
    f.write((data))
img.close()

