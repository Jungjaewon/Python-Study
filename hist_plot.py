import matplotlib.pyplot as pl
import numpy as np

a = np.array([-0.86906864, -0.72122614, -0.18074998, -0.57190212, -0.25689268 ,-1. ,0.68713553 ,0.29597819, 0.45022949, 0.37550592, 0.86906864, 0.17437203, 0.48704826, 0.2235648, 0.72122614, 0.14387731, 0.94194514])

fig = pl.hist(a,normed=0)
pl.title('Mean')
pl.xlabel("value")
pl.ylabel("Frequency")
pl.show()