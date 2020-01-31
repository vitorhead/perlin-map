import numpy as np
from PIL import Image
from noise import pnoise2

shape = (1024, 1024)
scale = 100.0

# colors
darkblue = (0,0,139)
lightblue = (173,216,230)
yellow = (238, 214, 175)
green = (34, 139, 34)
darkgreen = (0,100,0)
lightbrown = (181, 101, 29)
darkbrown = (150, 75, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (65, 105, 225)
grey = (139, 137, 137)


def generate_array():
	world = np.zeros(shape)
	for i in range(shape[0]):
		for j in range(shape[1]):
			world[i][j] = pnoise2(i/scale,
				j/scale,
				octaves=6,
				persistence=0.5,
				lacunarity=2.0,
				repeatx=1024,
				repeaty=1024,
				base=0)
    
	#for x in range(5):
	#    print(world[x][0:6])

	return world

def get_color(num):
    if num < -0.05:
        return blue
    elif num < 0.055:
        return yellow
    elif num < 0.25:
        return green
    elif num < 0.6:
    	return darkgreen
    elif num < 0.7:
    	return grey
    elif num < 1.0:
    	return white

def generate_map():
	world = generate_array()
	img = Image.new('RGB', shape)
	pixels = img.load()
	for i in range(shape[0]):
		for y in range(shape[1]):
			pixels[i, y] = get_color(world[i][y])
	img.save("generated_map.png")


generate_map()