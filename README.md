# Pylab
## Introduction
Image deconvolution is the act of uncovering the ground truth image through removing the various Point Spread Function (PSF) that are applied to each image. These techniques have particular relevance in fields such as signal processing, astronomy, microscopy, and even on our phones when we take pictures.

## Richardson-Lucy Deconvolution
The base algorithm that will be used is called Richardson-Lucy Deconvolution. It is a form of iterative deconvolution that transforms the image and a given PSF into the frequency domain using the DFFT (Discrete Fast Fourier Trransform). Including some noise tolerance, the algorithm subtracts the effects of the point spread function iterativley over a given number of iterations. Once terminated, the resulting image will be the ground truth image in theory, given some small error threshold.

### Blind Deconvolution
Blind deconvolution is when we are given a convolved image but no corresponding PSF. Here we must estimate a valid PSF iterativley using bayesian techniques. We must give the algorithm an initial PSF, which will be by default a 3x3 array of ones. 

## Setup
### Requirements
This package requires an instlation of Python 3.6, 3.7, or 3.8 as those are the only verisons of Python compaible with the engine.

This package requires that you have a working version of MATLAB 2020b or later installed on your computer. Once installed, follow the isntructions [here](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) to isntall the MATLAB API.

In addition to this your MATLAB distribution must include the Image Processing Toolbox instructions to download can be found [here](https://www.mathworks.com/help/matlab/matlab_env/get-add-ons.html#:~:text=To%20find%20and%20install%20add,list%20of%20available%20add%2Dons.&text=To%20install%20an%20add%2Don,from%20the%20available%20install%20actions.)

### Setup
Using the matlabroot path that was needed for the package installation, copy it for later use. This will be used for the pylab setup.py installation of the package. 

` python setup.py --install matlabroot `






