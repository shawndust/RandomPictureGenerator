from random import randrange
from PIL import Image
import math
import random

dim = 255
numDigits = 20000

def generateBlackAndWhitePicture(t):
    img = Image.new( 'RGB', (dim,dim), "black") # Create a new black image
    pixels = img.load() # Create the pixel map
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((t)//(2**(i+j*dim))%2 == 0):
                # print(t)
                blackOrWhite = 0
            else:
                blackOrWhite = 255
            pixels[i,j] = (blackOrWhite, blackOrWhite, blackOrWhite) # Set the colour accordingly
    img.show()

n = random.randint(10**(numDigits-1), (10**numDigits)-1)

for t in range(n, n+2):
    generateBlackAndWhitePicture(t)
