import numpy as np



if __name__ == '__main__':

    a = [['a','b','c'],['d','a','c'],['e','s','e']]

    print a
    print a[0]
    print type(a)
    print type(np.array(a))

    b = np.array(a)
    print b
    print b[0]
    print type(b[0])
    print type(b[1])
    print type(b[2])