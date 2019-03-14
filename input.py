import tensorflow as tf



def test_fun():

    print('function call')


if __name__ == '__main__':

    x = input('test : ')

    print(x)

    '''
    input = test_fun

    print input

    x = input('test : ')

    print x
    '''

    input = tf.placeholder("int32", [1], name="p")

    print(input())

