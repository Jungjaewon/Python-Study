import numpy as np





array = np.array([1])

print type(array[0])
print np.shape(array)
print np.shape(array[0])


i = array[0].item()
print type(i)
print i

print type(np.asscalar(array[0]))