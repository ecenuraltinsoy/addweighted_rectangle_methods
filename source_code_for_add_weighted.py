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
