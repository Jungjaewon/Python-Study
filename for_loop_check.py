import numpy as np



if __name__ == '__main__':

    num_items = 5
    num_source = 3
    num_target = 1
    dataset = []
    for i in range(1, num_items + 1):
        print i
        target_num = i
        target_label = np.zeros([num_items])
        target_label[i - 1] = 1

        source_list = range(1, num_items + 1)
        source_list.remove(target_num)

        k = 0
        while True:
            partial_source = source_list[k:k+num_source]
            if len(partial_source) != num_source:
                break
            else:
                add_list = []
                for j in partial_source:
                    temp_num = j
                    temp_label = np.zeros([num_items])
                    temp_label[j - 1] = 1
                    add_list.append([temp_num, temp_label])

                dataset.append([0, [target_num, target_label], add_list])
                k += 1

    print len(dataset)
    for item in dataset:
        print item