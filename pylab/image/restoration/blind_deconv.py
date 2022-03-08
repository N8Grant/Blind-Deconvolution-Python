import matlab.engine
import matlab
import numpy as np
import PIL
import matplotlib.pyplot as plt
import sys

print(sys.version_info[0:2])

if sys.version_info[0:2] != (3, 8) and sys.version_info[0:2] != (3, 7) and sys.version_info[0:2] != (3, 6):
    raise Exception('Requires python 3.6, 3.7, or 3.8')

eng = matlab.engine.start_matlab()

def blind_deconvolution(image, kernel_size=3, num_iterations=30, weighted=False, edge_weight=.08):
    # If URL to image
    if type(image) == type(str()):
        image = PIL.Image.open(image)
        image = PIL.ImageOps.grayscale(image)
    # If PIL image object
    elif type(image) == PIL.Image:
        image = np.asarray(image)
        image = PIL.ImageOps.grayscale(image)
    # If its already in numpy array
    elif type(image) == np.ndarray:
        image = PIL.Image.fromarray(image)
        image = PIL.ImageOps.grayscale(image)
    # Else raise exception
    else: 
        raise Exception('Input was of type ' + str(type(image)) + '. Must be a URL to an image, a PIL Image object, or an np array')
    
    # If weighted
    if weighted:
        weight = eng.edge(image,"sobel",edge_weight)
        se = eng.strel("disk",2)
        weight = 1-matlab.double(eng.imdilate(weight,se))

    # Starting kernel
    start_kernel_np = np.ones((kernel_size,kernel_size))
    start_kernel = []
    image_np = np.asarray(image)
    image = []

    # Convert to matlab types
    for i in range(len(start_kernel_np)):
        start_kernel.append(matlab.double(start_kernel_np[i].tolist()))  

    start_kernel = matlab.double(start_kernel)

    for i in range(len(image_np)):
        image.append(matlab.double(image_np[i].tolist()))
        
    image = matlab.double(image)

    # Call Matlab Blind deconvolution
    if weighted:
        deconvolved = eng.deconvblind(image, start_kernel, num_iterations, weight)
    else:
        deconvolved = eng.deconvblind(image, start_kernel)
    deconvolved = np.asarray(deconvolved).squeeze()

    return deconvolved