"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import csv
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
import cPickle as cp
import operator

flags = tf.app.flags

phase = 'test'
dataset = 'imagenet'
flags.DEFINE_string('csv_input', '/home/woodcook486/' + dataset + '_' + phase + '.csv', 'Path to the CSV input')
flags.DEFINE_string('output_path', '/home/woodcook486/' + dataset + '_' + phase + '.record', 'Path to output TFRecord')
flags.DEFINE_string('pbtxt_out_path', '/home/woodcook486/'+ dataset + '.pbtxt', 'Path to output Pbtxt')
flags.DEFINE_string('obj_pickle_path', '/home/woodcook486/py-faster-rcnn/data/' + dataset + '/' + dataset + '_object.pickle', 'Path to object pickle')
FLAGS = flags.FLAGS

#global sorted_Objmapping
#global Obj_mapping

with open(FLAGS.obj_pickle_path, 'r') as fp:
    Obj_mapping = cp.load(fp)
    sorted_Objmapping = sorted(Obj_mapping.items(), key=operator.itemgetter(0))
    reverse_obj_mapping = {v: k for k, v in Obj_mapping.iteritems()}



def create_tf_example(line):

    try:
        path = '/home/woodcook486/py-faster-rcnn/data/' + dataset + '/Images/'
        with tf.gfile.GFile(os.path.join(path, line[0]) , 'rb') as fid:
            encoded_jpg = fid.read()
    except:
        print('image is not here!!!')

    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size
    filename = str(line[0] + '.jpg').encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes = []
    xmins.append(float(line[1]) / width)
    ymins.append(float(line[2]) / height)
    xmaxs.append(float(line[3]) / width)
    ymaxs.append(float(line[4]) / height)
    classes_text = bytes(line[5])
    classes.append(int(line[6]))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))

    return tf_example

'''
item {
  id: 1
  name: 'raccoon'
}
'''
def save_label_map_as_Pbtxt():
    with open(FLAGS.pbtxt_out_path,'w') as f:
        for line in sorted_Objmapping:
            #print('item {')
            #print('  id: ' + str(l[1]))
            #print('  name: ' + l[0])
            #print('}')
            if line[0] == 0:
                print(line)
                continue

            f.write('item {\n')
            f.write('  id: ' + str(line[0]) + '\n')
            f.write('  name: \'' + line[1]+ '\'\n')
            f.write('}'+'\n')

def main(_):

    #writer = tf.python_io.TFRecordWriter(FLAGS.output_path)

    save_label_map_as_Pbtxt()

    #make tfrecord
    '''
        with open(FLAGS.csv_input) as f:
        examples = csv.reader(f)

        for line in examples:

            tf_example_s = create_tf_example(line)
            if tf_example_s == -1:
                print('data Error!!')
                continue
            writer.write(tf_example_s.SerializeToString())

        writer.close()

        print('Successfully created the TFRecords: {}'.format(FLAGS.output_path))
    '''




if __name__ == '__main__':
    tf.app.run()
