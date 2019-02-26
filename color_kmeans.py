#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:35:05 2018

@author: Huilin
"""

print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

n_colors = 5

# Load the photo
im = Image.open('/Users/tian/Desktop/untitled folder/高阶水色拉伸/20180531-小吉浦(全段)_90mcolor.jpg')

# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])
im = np.array(im, dtype=np.float64) / 255

# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(im.shape)
assert d == 3
image_array = np.reshape(im, (w * h, d))
# Set training set as random 10000
image_array_sample = shuffle(image_array, random_state=0)[:10000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)

# Get labels for all points
labels_500 = kmeans.predict(image_array)


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

plt.figure()
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels_500, w, h))
plt.savefig('color_kmeans.png')

