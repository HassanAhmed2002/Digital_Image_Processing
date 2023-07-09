import matplotlib.pyplot as plt
from skimage import color, data
from skimage.transform import rescale
image = color.rgb2gray(data.astronaut())

image_rescaled = rescale(image, 0.25, anti_aliasing=False)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("Original image")

ax[1].imshow(image_rescaled, cmap=plt.cm.gray)
ax[1].set_title("Downscaled image (4 times smaller)")

for a in ax:
    a.axis("off")

plt.show()