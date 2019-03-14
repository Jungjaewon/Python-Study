import shutil
import os.path

def merging_data(src_annotations,src_images, src_imagesets, dataset):

    home = '/home/woodcook486/'

    dest_annotations = home + 'vrd/Annotations/'
    dest_images = home + 'vrd/Images'
    dest_imagesets = home + 'vrd/ImageSets'

    with open(src_imagesets + 'train.txt','r') as fp:
        train_list = fp.readlines()
    with open(src_imagesets + 'train.txt','r') as fp:
        test_list = fp.readlines()

    for i in range(len(train_list)):
        train_list[i] = train_list[i].strip()

    for i in range(len(test_list)):
        test_list[i] = test_list[i].strip()

    if dataset == 'imagenet':
        imext = '.JPEG'
    else:
        imext = '.jpg'

    for im in train_list:

        src_xml = src_annotations + im + '.xml'
        assert os.path.isfile(src_xml)
        dest_xml = dest_annotations + im + '.xml'
        shutil.copy(src_xml, dest_xml)

        src_im = src_images + im + imext
        assert os.path.isfile(src_xml)
        dest_im = dest_images + im +imext
        shutil.copy(src_im, dest_im)

    for im in test_list:

        src_xml = src_annotations + im + '.xml'
        assert os.path.isfile(src_xml)
        dest_xml = dest_annotations + im + '.xml'
        shutil.copy(src_xml, dest_xml)

        if dataset == 'imagenet':
            imext = '.JPEG'
        else:
            imext = '.jpg'
        src_im = src_images + im + imext
        assert os.path.isfile(src_xml)
        dest_im = dest_images + im +imext
        shutil.copy(src_im, dest_im)

    with open(dest_imagesets + 'train.txt','a') as fp:
        for im in train_list:
            fp.write(im + '\n')

    with open(dest_imagesets + 'test.txt','a') as fp:
        for im in test_list:
            fp.write(im + '\n')


if __name__ == '__main__':

    home = '/home/woodcook486/'

    dest_annotations = home + 'vrd/Annotations/'
    dest_images = home + 'vrd/Images'
    dest_imagesets = home + 'vrd/ImageSets'

    coco_annotations = home + 'cocoapi/vrd/Annotations/'
    coco_images = home + 'cocoapi/vrd/Images/'
    coco_imagesets = home + 'cocoapi/vrd/ImageSets/'

    merging_data(coco_annotations, coco_images, coco_imagesets, 'coco')

    imagenet_annotations = home + 'imagenet_vrd/Annotations/'
    imagenet_images = home + 'imagenet_vrd/Images/'
    imagenet_imagesets = home + 'imagenet_vrd/ImageSets/'

    merging_data(imagenet_annotations, imagenet_images, imagenet_imagesets, 'imagenet')

    vrd_annotations = home + 'py-faster-rcnn/data/vrd/Annotations/'
    vrd_images = home + 'py-faster-rcnn/data/vrd/Images/'
    vrd_imagesets = home + 'py-faster-rcnn/data/vrd/ImageSets/'

    merging_data(vrd_annotations, vrd_images, vrd_imagesets, 'vrd')


