from PIL import Image

def process(filename, savename):
    im = Image.open(filename)
    pixels = im.load()
    #sneg = im.open('resources/sneg.jpg')
    for i in range(im.width):
        for j in range(im.height):
            r,g,b = pixels[i,j]
            a = (r+g+b)//3
            pixels[i, j]=(a,a,b)
    im.save(savename)