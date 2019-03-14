
import os

def search(dirname):
    filenames = os.listdir(dirname)
    max = -1
    maxFile_name = ''
    for filename in filenames:
        split = filename.split('.')
        if split[-1] =='log':
            pass
        else:
            print 'here'
            continue
        full_filename = os.path.join(dirname, filename)
        print (full_filename)

        with open(full_filename,'r') as fp:

            lines = fp.readlines()
            map = lines[-10].split(' = ')

            MeanAp = float(map[-1].strip())
            if MeanAp > max:
                max = MeanAp
                maxFile_name = full_filename


    print max, ' ', maxFile_name



if __name__ == '__main__':
    search("test")