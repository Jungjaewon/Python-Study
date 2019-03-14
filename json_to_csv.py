import json
import csv
import json
import cPickle as cp


def rel_dict_generator(jsonfile):
    unique_filelist = []

    rel_dic = {}

    for rel in jsonfile:
        filename = rel['filename'].split('/')[-1]
        file_wo_ex = filename.split('.')[0]
        unique_filelist.append(file_wo_ex)

    unique_filelist = list(set(unique_filelist))

    for filename in unique_filelist:
        for rel in jsonfile:
            file = rel['filename'].split('/')[-1]
            file_wo_ex = file.split('.')[0]

            if filename == file_wo_ex:
                if rel_dic.has_key(filename):
                    rel_dic[filename].append(rel)
                else:
                    rel_dic[filename] = []
                    rel_dic[filename].append(rel)
    return rel_dic

def json_to_csv(inJsonFileName, outJsonFileName, dataset):

    print 'reading %s ...' % (inJsonFileName)

    with open(inJsonFileName,'r') as fp:
        inRelJson = json.load(fp)
    print 'json read done'

    with open('/home/woodcook486/py-faster-rcnn/data/' + dataset + '/' +  dataset + '_object.pickle', 'r') as fp:
        obj_mapping_dict = cp.load(fp)

    csv_data = []

    rel_dict = rel_dict_generator(inRelJson)


    for im_name in rel_dict:

        im_rel_list = rel_dict[im_name]

        so_list = []
        dup_list = []
        unique_list = []

        for rel in im_rel_list:
            so_list.append([rel['subject'], rel['label_phrase'][0]])
            so_list.append([rel['object'],  rel['label_phrase'][2]])

        for i in range(len(so_list)):
            A = so_list[i]
            for j in range(i + 1, len(so_list)):
                B = so_list[j]
                A_box = A[0]
                B_box = B[0]
                # A[1], B[1] Label
                # box x1 y1 x2 y2
                if A[1] == B[1] and A_box[0] == B_box[0] and A_box[1] == B_box[1] and A_box[2] == B_box[2] \
                        and A_box[3] == B_box[3]:
                    dup_list.append(j)

        for i in range(len(so_list)):
            if i in dup_list:
                continue
            else:
                unique_list.append(so_list[i])

        for item in unique_list:
            csv_data.append([im_name,item[0],item[1]])



    with open(outJsonFileName,'w') as fp:

        csv_writer = csv.writer(fp)
        #csv_writer.writerow(['image', 'xmin', 'ymin', 'xmax', 'ymax', 'class_name', 'class_label'])
        for line in csv_data:
            box = line[1]
            cls_label = line[2]
            csv_writer.writerow([line[0] + '.jpg',box[0],box[1],box[2],box[3],obj_mapping_dict[cls_label],cls_label])


if __name__ == "__main__":

    dataset_list = ['vrd', 'svg', 'imagenet', 'coco', 'vrd_p']
    set_list = ['_train', '_test']

    for dataset in dataset_list:
        for phase in set_list:
            inJsonFileName = '/home/woodcook486/py-faster-rcnn/data/' + dataset + '/' + dataset + phase + '.json'
            outCSVFileName = inJsonFileName.split('.')[0]+str('.csv')
            json_to_csv(inJsonFileName, outCSVFileName, dataset)
