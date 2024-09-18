import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
    
def create_image_array(image_path):

    with Image.open(image_path) as img:
        return np.array(img)
    
def clip(value, min_value, max_value):
    
    return min(max(value, min_value), max_value)

def add_weighted(image1, alpha, image2, beta, gamma):

    if image1.shape != image2.shape:
        raise ValueError("Images must be equal in size.")
    
    result = alpha * image1 + beta * image2
    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(result.shape[2]):
                result[i, j, k] = clip(result[i, j, k] + gamma, 0, 255)
    
    result = result.astype('uint8')
    
    return result

image_sea = create_image_array("C:\\Users\\USER\\Desktop\\Cmpe_362\\Deneme\\sea.jpg") 
image_desert = create_image_array("C:\\Users\\USER\\Desktop\\Cmpe_362\\Deneme\\desert.jpg")

alpha = 0.5
beta = 0.5
gamma = 0
combined_image = add_weighted(image_sea, alpha, image_desert, beta, gamma)

import matplotlib.pyplot as plt

plt.imshow(combined_image)
plt.show()