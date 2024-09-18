import matplotlib.pyplot as plt
from PIL import Image
  
def create_image_array(image_path):
    
    with Image.open(image_path) as img:
        return np.array(img)

def rectangle(image, start_point, end_point, color, thickness):
    
    start_x, start_y = start_point
    end_x, end_y = end_point
    
    if thickness != -1:
        
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                
                if (start_y <= y < start_y + thickness or end_y - thickness <= y < end_y):
                    image[y][x] = color
                if (start_x <= x < start_x + thickness or end_x - thickness <= x < end_x):
                    image[y][x] = color
    else:
        
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                image[y][x] = color

    return image

import numpy as np

image = create_image_array("C:\\Users\\USER\\Desktop\\Cmpe_362\\Deneme\\parrot.jpg")

start_point = (750, 200)
end_point = (1350, 700)
color = (255, 0, 0) 
thickness = 10 

drawn_image = rectangle(image, start_point, end_point, color, thickness)

import matplotlib.pyplot as plt

plt.imshow(drawn_image)
plt.show()