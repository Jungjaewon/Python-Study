import json
from random import shuffle


def limit_num_dataset(folder,jsonfile, num):

    with open(folder + jsonfile) as fp:
        Rel = json.load(fp)

    shuffle(Rel)
    shuffle(Rel)
    new_dataset = Rel[:num]

    with open(folder + 'limit_num' + str(num) + '_' + jsonfile,'w') as fp:
        json.dump(new_dataset,fp,indent=3)

def limit_prd_dataset(folder, jsonfile, prd):

    new_dataset = []
    with open(folder + jsonfile) as fp:
        Rel = json.load(fp)

    shuffle(Rel)
    shuffle(Rel)

    for rel in Rel:

        if rel['phrase'][0] == prd :
            new_dataset.append(rel)

    with open(folder + 'limit_num' + str(prd) + '_' + jsonfile, 'w') as fp:
        json.dump(new_dataset, fp, indent=3)

def limit_num_prd_dataset(folder , jsonfile, num,prd):

    new_dataset = []
    with open(folder + jsonfile) as fp:
        Rel = json.load(fp)

    shuffle(Rel)
    shuffle(Rel)

    for rel in Rel:
        if rel['phrase'][0] == prd:
            new_dataset.append(rel)

    shuffle(new_dataset)
    shuffle(new_dataset)

    new_dataset = new_dataset[:num]

    with open(folder + 'limit_num' + str(prd) + '_' + str(num) + '_' + jsonfile, 'w') as fp:
        json.dump(new_dataset, fp, indent=3)


if __name__ == '__main__':
    pass