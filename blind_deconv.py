#!/usr/bin/env python3

import matlab
import numpy
import PIL
import matplotlib.pyplot as plt
import sys

if sys.version_info[0:2] != (3, 8):
    raise Exception('Requires python 3.8')

class BlindDeconv():
    def __init__(self, matlab_python_engine):
        self.matlab = matlab.MatlabSession(matlab_root=matlab_python_engine)

    def blind_deconvolution(self, image, kernel_size=3, num_iterations=30, weighted=False, edge_weight=.08):
        # If URL to image
        if type(image) == type(str()):
            image = np.asarray(PIL.Image.open(image))
        # If PIL image object
        elif type(image) == PIL.Image:
            image = np.asarray(image)
        # If its already in numpy array
        elif type(image) == np.ndarray:
            continue
        # Else raise exception
        else: 
            raise Exception('Input was of type ' + str(type(image)) + '. Must be a URL to an image, a PIL Image object, or an np array')
        
        # If weighted
        if weighted:
            weight = self.matlab.workspace.edge(image,"sobel",edge_weight)
            se = self.matlab.workspace.strel("disk",2)
            weight = 1-double(self.matlab.workspace.imdilate(weight,se))
     
            #weight([1:3 end-(0:2)],:) = 0
            #weight(:,[1:3 end-(0:2)]) = 0

        # Starting kernel
        start_kernel = np.ones((kernel_size,kernel_size))

        # Convert to matlab types
        starting_kernel = matlab.double(starting_kernel.tolist())
        image = matlab.double(image.tolist())

        # Call Matlab Blind deconvolution
        if weighted:
            deconvolved, psf = self.matlab.workspace.deconvblind(image, start_kernel, num_iterations,weight)
        else:
            deconvolved, psf = self.matlab.workspace.deconvblind(image, start_kernel, num_iterations)
        deconvolved = np.asarray(deconvolved)

        def save(self,URL):
            deconvolved = PIL.Image.save(URL)

        def show(self):
            plt.imshow(deconvolved)
            plt.show()

        return deconvolved