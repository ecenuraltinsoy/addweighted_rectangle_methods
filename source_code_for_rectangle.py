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
