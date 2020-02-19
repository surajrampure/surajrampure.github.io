import matplotlib.pyplot as plt
from align_image_code import align_images
import skimage as sk
import skimage.io as skio

# First load images

name1 = 'me copy.jpeg'
name2 = 'littleme.jpeg'

# high sf
im1 = plt.imread('raw/' + name1)/255.

# low sf
im2 = plt.imread('raw/' + name2)/255

# Next align images (this code is provided, but may be improved)
im1_aligned, im2_aligned = align_images(im1, im2)

skio.imsave('aligned/' + name1, im1_aligned)
skio.imsave('aligned/' + name2, im2_aligned)

# ## You will provide the code below. Sigma1 and sigma2 are arbitrary 
# ## cutoff values for the high and low frequencies

# sigma1 = arbitrary_value_1
# sigma2 = arbitrary_value_2
# hybrid = hybrid_image(im1, im2, sigma1, sigma2)

# plt.imshow(hybrid)
# plt.show

# ## Compute and display Gaussian and Laplacian Pyramids
# ## You also need to supply this function
# N = 5 # suggested number of pyramid levels (your choice)
# pyramids(hybrid, N)