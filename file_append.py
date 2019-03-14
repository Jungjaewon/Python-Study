
def append():

    with open('append.txt','a') as fp:
        fp.write('this is a append test\n')

    with open('append.txt','a') as fp:
        fp.write('this is a second append test\n')
if __name__ == '__main__':
    append()