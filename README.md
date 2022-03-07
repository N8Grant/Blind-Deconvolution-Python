# BlindDeconvolutionPython
## Introduction
Image deconvolution is the act of uncovering the ground truth image through removing the various Point Spread Function (PSF) that are applied to each image. These techniques have particular relevance in fields such as signal processing, astronomy, microscopy, and even on our phones when we take pictures.

## Richardson-Lucy Deconvolution
The base algorithm that will be used is called Richardson-Lucy Deconvolution. It is a form of iterative deconvolution that transforms the image and a given PSF into the frequency domain using the DFFT (Discrete Fast Fourier Trransform). Including some noise tolerance, the algorithm subtracts the effects of the point spread function iterativley over a given number of iterations. Once terminated, the resulting image will be the ground truth image in theory, given some small error threshold.

## Blind Deconvolution
Blind deconvolution is when we are given a convolved image but no corresponding PSF. Here we must estimate a valid PSF iterativley using bayesian techniques. One drawback is that since the likliehood landscape is nonconvex, we could get stuck in a local maximum, not actually getting to the ground truth image after the process completes.

## Uses MATLAB Wrapper
Using a matlab wrapper, this package will convert python types to c types to be fed into MATLAB for deconvolution. The resulting image will then be output as a numpy array.
