import json
import numpy as np

def get_sig_dataset_so_p(folder, jsonfile):

    num_prd = 70
    num_obj = 100
    with open(folder + jsonfile,'r') as fp:
        Rel = json.load(fp)

    so_dict = {}
    po_dict = {}
    sp_dict = {}

    for rel in Rel:

        phrase = rel['phrase']
        sbj = phrase[0]
        prd = phrase[1]
        obj = phrase[2]

        sbob = sbj+ '*' + obj

        if so_dict.has_key(sbob):
            so_dict[sbob].append(rel['label_phrase'][1])
        else:
            so_dict[sbob] = []
            so_dict[sbob].append(rel['label_phrase'][1])

        prdobj = prd + '*' + obj

        if po_dict.has_key(prdobj):
            po_dict[prdobj].append(rel['label_phrase'][0])
        else:
            po_dict[prdobj] = []
            po_dict[prdobj].append(rel['label_phrse'][0])

        sbjprd = sbj + '*' + prd

        if sp_dict.has_key(sbjprd):
            sp_dict.append(rel['label_phrase'][2])
        else:
            sp_dict[sbjprd] = []
            sp_dict.append(rel['label_phrase'][2])

    for key in so_dict:

        veclist = list(set(so_dict[key]))
        bi_vector = np.zeros(num_prd)

        for idx in veclist:
            bi_vector[idx] = 1

        assert len(veclist) == np.sum(bi_vector)

        so_dict[key] = bi_vector.tolist()

    for key in po_dict:

        veclist = list(set(po_dict[key]))
        bi_vector = np.zeros(num_obj)

        for idx in veclist:
            bi_vector[idx] = 1

        assert len(veclist) == np.sum(bi_vector)

        po_dict[key] = bi_vector.tolist()

    for key in sp_dict:

        veclist = list(set(sp_dict[key]))
        bi_vector = np.zeros(num_obj)

        for idx in veclist:
            bi_vector[idx] = 1

        assert len(veclist) == np.sum(bi_vector)

        sp_dict[key] = bi_vector.tolist()

    newRel = []

    for rel in Rel:

        nrel = rel

        phrase = nrel['phrase']
        sbj = phrase[0]
        prd = phrase[1]
        obj = phrase[2]
        sbob = sbj + '*' + obj
        prdobj = prd + '*' + obj
        sbjprd = sbj + '*' + prd

        assert so_dict.has_key(sbob)
        assert po_dict.has_key(prdobj)
        assert sp_dict.has_key(sbjprd)

        nrel['bivec_so'] = so_dict[sbob]
        nrel['bivec_po'] = po_dict[prdobj]
        nrel['bivec_sp'] = so_dict[sbjprd]
        newRel.append(nrel)

    new_filename = 'sigmoid_' + jsonfile
    with open(new_filename,'w') as fp:
        json.dump(newRel,fp,indent=3)

if __name__ == '__main__':
    pass