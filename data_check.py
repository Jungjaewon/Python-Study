import json


def load_annotation(folder, jsonTrain, jsonTest):

    with open(folder + '/' + jsonTrain) as fp:
        RelTrain = json.load(fp)

    with open(folder + '/' + jsonTest) as fp:
        RelTest = json.load(fp)


    train_list = []
    test_list = []
    train_cnt = 0
    for image in RelTrain:

        train_cnt += len(RelTrain[image])

        rel_list = RelTrain[image]
        for item in rel_list:
            train_list.append(item)



    #print train_cnt

    test_cnt = 0

    for image in RelTest:

        test_cnt += len(RelTest[image])

        rel_list = RelTest[image]

        for item in rel_list:
            test_list.append(item)


    print len(train_list)
    print len(test_list)
    zs_list = []
    flag = False

    for test_rel in test_list:

        test_prd = test_rel['predicate']
        test_sbj = test_rel['subject']['category']
        test_obj = test_rel['object']['category']


        for train_rel in train_list:
            train_prd = train_rel['predicate']
            train_sbj = train_rel['subject']['category']
            train_obj = train_rel['object']['category']

            if (test_prd == train_prd) and (test_sbj == train_sbj) and (test_obj == train_obj):
                flag = True

        if flag is False:
            zs_list.append(test_rel)
        flag = False

    print len(zs_list)


    for zitem in zs_list:

        assert  zitem in test_list

    #print test_cnt
if __name__ == '__main__':
    load_annotation('vrd_check','annotations_train.json','annotations_test.json')
