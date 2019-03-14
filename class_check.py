
def main(vrdfile, classfile):
    pass
    vrd_list = []
    class_list = []

    with open(vrdfile,'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            else:
                line_list = line.split(' ')
                item = line_list[-1].split('\n')[0]
                vrd_list.append(item)
    #print vrd_list
    with open(classfile, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            else:
                item = line.split('\n')[0]
                class_list.append(item)
    #print class_list
    hit = 0
    for item in vrd_list:
        if item in class_list:
            hit += 1

    print '# of vrd class is ', hit ,'in ', classfile



if __name__ =='__main__':
    pass
    main('vrd_object.txt','coco_class.txt')
    main('vrd_object.txt', 'imagenet_class.txt')