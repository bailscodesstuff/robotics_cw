import matplotlib.pyplot as plt 

def boundingbox(image, coords, height, width):
    x1, y1, x2, y2 = coords

    x1 = int(round(x1 * width))
    x2 = int(round(x2 * width))
    y1 = int(round(y1 * height))
    y2 = int(round(y2 * height))
    
    box = image[y1:y2, x1:x2]
    plt.imshow(box)
    

# start of extracting bounding box from image
