import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_path = 'ddog.jpg'
img = mpimg.imread(image_path)

if img is None:
    print(f"Error: Unable to load the image at {image_path}")
else:
    gray_img = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Picture')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.show()