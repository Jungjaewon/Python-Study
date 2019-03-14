import json


def get_faster_rcnn_dataset(rel_test, rel_train):

    with open(rel_test,  'r') as fp:
        test_json = json.load(fp)
    with open(rel_train, 'r') as fp:
        train_json = json.load(fp)

    for rel in test_json:
        print rel




if __name__ == '__main__':
    all_file = get_faster_rcnn_dataset('rel_test.json', 'rel_train.json')