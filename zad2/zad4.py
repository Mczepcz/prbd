import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.colors as colors
import numpy as np 
import os
import zad3 as reducer

img = image.imread('resources'+os.sep+'lab2'+os.sep+'meil.png')
size = 20

scaledImage = np.zeros((size,size,3))
red = reducer.reduce(img[:, :, 0], (size,size))
green = reducer.reduce(img[:, :, 1], (size,size))
blue = reducer.reduce(img[:, :, 2], (size,size))
scaledImage[:, :, 0] = red
scaledImage[:, :, 1] = green
scaledImage[:, :, 2] = blue

_, (a1,a2) = plt.subplots(1,2)
a1.imshow(img)
a2.imshow(scaledImage)

plt.show()

hsvImage = colors.rgb_to_hsv(scaledImage)
hsvImage[:, :, 1] = 0

dark = np.zeros((size, size), dtype=bool)
light = np.copy(dark)

for i in range(size):
    for j in range(size):
        if hsvImage[i, j, 2] < 0.3:
            dark[i, j] = True
        elif hsvImage[i, j][2] < 0.6:
            light[i, j] = True

with open('logo.txt', 'w') as f:
    for d, l in zip(dark, light):
        line = np.array(["  "]*size)
        line[d] = "||"
        line[l] = "- "
        f.write("".join(line))
        f.write("\n")