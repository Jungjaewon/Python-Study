import numpy as np
import cv2


if __name__ == '__main__':

    colormap = np.zeros((256, 3), dtype=int)
    ind = np.arange(256, dtype=int)

    for shift in reversed(range(8)):
        for channel in range(3):
            colormap[:, channel] |= ((ind >> channel) & 1) << shift
        ind >>= 3

    #print colormap

    label = np.ones((30,30),dtype=int)

    print label.ndim
    print colormap[label]
    print np.shape(colormap[label])