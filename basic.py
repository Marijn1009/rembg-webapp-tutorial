from rembg import remove
from PIL import Image


input = Image.open('verhaeg_marijn.jpg')

output = remove(input)

output.save('out.png')