import cv2
import os.path as osp
import numpy as np
import glob
import os
import argparse
import threading
import time

# sem_cate = threading.Semaphore()
# sem_color = threading.Semaphore()
mutex_cate = threading.Lock()
mutex_color = threading.Lock()


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--test_folder', dest='test_folder', help='test_txt', default='', type=str)

    '''
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    '''

    args = parser.parse_args()
    return args


def parse_file(str1, str2):
    pstr1 = str1.split('/')[-1].split('_')[-1]
    pstr2 = str2.split('/')[-1].split('_')[-1]

    assert pstr1 == pstr2

    return pstr1


def find_index(b, g, r, colormap):
    for i in range(len(colormap)):
        if colormap[i][0] == r and colormap[i][1] == g and colormap[i][2] == b:
            return i

    # print r,g,b
    return None
    # assert 'Colormap error!!'


def mapping_thread(th_num, key, color_img, location_list, cate_mapping):
    for location in location_list:
        x, y = location

        b = color_img[x][y][0]
        g = color_img[x][y][1]
        r = color_img[x][y][2]
        ind = find_index(b, g, r, color_colormap)
        if ind is None:
            # print ind
            print('th_num : ', th_num, 'color ind is None')
            continue

        mutex_cate.acquire()
        if cate_mapping[key].has_key(ind):
            cate_mapping[key][ind] += 1
        else:
            cate_mapping[key][ind] = 1
        mutex_cate.release()
        time.sleep(0.001)


def category_thread(th_num, cate_img, start_w, end_w, start_h, end_h, cate_class, cate_colormap):
    for i in range(start_w, end_w):
        for j in range(start_h, end_h):
            mutex_color.acquire()
            b = cate_img[i][j][0]
            g = cate_img[i][j][1]
            r = cate_img[i][j][2]
            ind = find_index(b, g, r, cate_colormap)

            if ind is None or ind is 0:
                if ind == 0:
                    continue
                print('th_num : ', th_num, 'cate ind is None')
                none_list.append([b, g, r])
                continue
            if cate_class.has_key(ind):
                cate_class[ind].append([i, j])
            else:
                cate_class[ind] = []
                cate_class[ind].append([i, j])
            mutex_color.release()
            time.sleep(0.001)


if __name__ == '__main__':

    args = parse_args()

    print('Called with args:')
    print(args)

    test_colorList = sorted(glob.glob(os.path.join(args.test_folder, 'seg_color_*.png')))

    # color_folder = '/home/woodcook486/deeplab_vis/vis_mcolor'
    # color_txt = '/home/woodcook486/tmm_dataset/ImageSets/category/test.txt'
    # color_root = osp.join(color_folder,'segmentation_results')
    # color_files = load_testlist(color_txt)

    test_cateList = sorted(glob.glob(os.path.join(args.test_folder, 'seg_category_*.png')))

    # category_folder = '/home/woodcook486/deeplab_vis/vis_category'
    # category_txt = '/home/woodcook486/tmm_dataset/ImageSets/category/test.txt'
    # category_root = osp.join(category_folder,'segmentation_results')
    # category_files = load_testlist(category_txt)

    # assert len(category_files) == len(color_files) and sorted(category_files) == sorted(color_files)
    assert len(test_cateList) == len(test_colorList)
    # print 'len(category_files)', len(category_files)
    cate_colormap = np.array([  # order b-g-r
        [0, 0, 0],  # bk 0
        [11, 102, 255],  # T-shirt 1
        [120, 120, 120],  # bag 2
        [180, 120, 120],  # belt 3
        [6, 230, 230],  # blazer 4
        [80, 50, 50],  # blouse 5
        [4, 200, 3],  # coat 6
        [120, 120, 80],  # dress 7
        [140, 140, 140],  # face 8
        [204, 5, 255],  # hair 9
        [230, 230, 230],  # hat 10
        [4, 250, 7],  # jeans 11
        [224, 4, 225],  # legging 12
        [235, 255, 7],  # pants 13
        [150, 5, 61],  # scarf 14
        [120, 120, 70],  # shoe 15
        [8, 255, 51],  # shorts 16
        [203, 192, 255],  # skin 17
        [143, 255, 140],  # skirt 18
        [204, 255, 4],  # socks 19
        [255, 51, 7],  # stocking 20
        [255, 51, 7],  # sunglass 21
        [61, 220, 250],  # sweater 22
    ])

    cate_class_list = ['bk', 'T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress',
                       'face', 'hair', 'hat', 'jeans', 'legging', 'pants', 'scarf', 'shoe',
                       'shorts', 'skin', 'skirt', 'socks', 'stocking', 'sunglass', 'sweater']

    color_colormap = np.array([  # order b-g-r
        [0, 0, 0],  # bk 0
        [220, 245, 245],  # beige 1
        [51, 0, 51],  # black 2
        [255, 0, 0],  # blue 3
        [42, 42, 165],  # brown 4
        [128, 128, 128],  # gray 5
        [0, 128, 0],  # green 6
        [0, 165, 255],  # orange 7
        [230, 192, 255],  # pink 8
        [128, 0, 128],  # purple 9
        [0, 0, 235],  # red 10
        [255, 255, 255],  # white 11
        [0, 255, 255],  # yellow 12
    ])

    color_class_list = ['bk', 'beige', 'black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red',
                        'white', 'yellow']

    upper_class = ['T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress', 'hat', 'scarf', 'sunglass', 'sweater']
    lower_class = ['jeans', 'legging', 'pants', 'shorts', 'socks', 'stocking', 'skirt']
    other_class = ['bk', 'face', 'hair', 'skin']

    none_list = []
    nThread = 20

    for i in range(len(test_colorList)):

        filename = parse_file(test_colorList[i], test_cateList[i])
        color_img = cv2.imread(test_colorList[i])
        cate_img = cv2.imread(test_cateList[i])

        cate_class = {}
        cate_mapping = {}
        (w, h, c) = cate_img.shape

        with_list = range(0, w, nThread)
        with_list.append(w)
        height_list = range(0, h, nThread)
        height_list.append(h)
        threads = []
        tn_cnt = 0
        for w_i in range(len(with_list)):
            if w_i + 1 == len(with_list):
                break
            for h_i in range(len(height_list)):
                if h_i + 1 == len(height_list):
                    break
                start_w = with_list[w_i]
                end_w = with_list[w_i + 1]
                start_h = height_list[h_i]
                end_h = height_list[h_i + 1]
                threads.append(threading.Thread(target=category_thread, args=(
                tn_cnt, cate_img, start_w, end_w, start_h, end_h, cate_class, cate_colormap)))
                tn_cnt += 1

        for thread in threads:  # Starts all the threads.
            thread.start()
        for thread in threads:  # Waits for threads to complete before moving on with the main script.
            thread.join()

        # cate_class { 0(category_class number) : {[[x1,y2],...[xn,yn]]}}
        threads = []
        tn_cnt = 0
        for key in cate_class:
            location_list = cate_class[key]
            threads.append(
                threading.Thread(target=mapping_thread, args=(th_num, key, color_img, location_list, cate_mapping)))
            tn_cnt += 1

        for thread in threads:  # Starts all the threads.
            thread.start()
        for thread in threads:  # Waits for threads to complete before moving on with the main script.
            thread.join()

        upper_str = str(filename.split('.')[0] + '.jpg') + ' upper' + ' '
        lower_str = str(filename.split('.')[0] + '.jpg') + ' lower' + ' '

        # print cate_mapping
        for key in cate_mapping:  # cate_mapping {0(cate_class) : {0(color_class) : 34, 1 : 10, ...etc}}
            # print key
            color_map = cate_mapping[key]

            tmp = 0
            k = 0
            for ckey in color_map:
                color_cnt = color_map[ckey]
                if color_cnt > tmp:  # equal??
                    tmp = color_cnt
                    k = ckey

            if cate_class_list[key] in upper_class:
                upper_str += str(cate_class_list[key]) + '-color-' + str(color_class_list[k]) + ' '
            elif cate_class_list[key] in lower_class:
                lower_str += str(cate_class_list[key]) + '-color-' + str(color_class_list[k]) + ' '
            elif cate_class_list[key] in other_class:
                pass

        with open('upper_seg.txt', 'a') as fp:
            fp.write(upper_str + '\n')
        with open('lower_seg.txt', 'a') as fp:
            fp.write(lower_str + '\n')
    # print none_list
    b = list()
    for sublist in none_list:
        if sublist not in b:
            b.append(sublist)
    print(b)















