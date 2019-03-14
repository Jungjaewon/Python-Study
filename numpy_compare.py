import numpy as np



if __name__ == '__main__':

    max_result = []
    batch_result = np.random.randn(70)
    result = np.random.randn(70)

    assert len(batch_result) == len(result)


    for i in range(len(batch_result)):

        if batch_result[i] > result[i]:
            max_result.append(batch_result[i])
        else:
            max_result.append(result[i])


    max_result = np.array(max_result)
    assert len(max_result) == len(batch_result)

