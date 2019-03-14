import numpy as np


def ranking_precision_score(y_true, y_score, k=10):
    """Precision at rank k

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).

    y_score : array-like, shape = [n_samples]
        Predicted scores.

    k : int
        Rank.

    Returns
    -------
    precision @k : float
    """
    unique_y = np.unique(y_true)
    if len(unique_y) > 2:
        raise ValueError("Only supported for two relevance levels.")

    pos_label = unique_y[1]
    n_pos = np.sum(y_true == pos_label)
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order[:k])
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.take.html
    n_relevant = np.sum(y_true == pos_label)

    # Divide by min(n_pos, k) such that the best achievable score is always 1.0.
    return float(n_relevant) / min(n_pos, k)


def average_precision_score(y_true, y_score, k=10):
    """Average precision at rank k

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Ground truth (true relevance labels).

    y_score : array-like, shape = [n_samples]
        Predicted scores.

    k : int
        Rank.

    Returns
    -------
    average precision @k : float
    """
    unique_y = np.unique(y_true)

    if len(unique_y) > 2:
        raise ValueError("Only supported for two relevance levels.")

    pos_label = unique_y[1]
    n_pos = np.sum(y_true == pos_label)

    order = np.argsort(y_score)[::-1][:min(n_pos, k)]
    y_true = np.asarray(y_true)[order]

    score = 0
    for i in xrange(len(y_true)):
        if y_true[i] == pos_label:
            # Compute precision up to document i
            # i.e, percentage of relevant documents up to document i.
            prec = 0
            for j in xrange(0, i + 1):
                if y_true[j] == pos_label:
                    prec += 1.0
            prec /= (i + 1.0)
            score += prec

    if n_pos == 0:
        return 0

    return score / n_pos

if __name__ == '__main__':
    # Precision
    pass
    #assert ranking_precision_score([1, 1, 0], [3, 2, 1], k=2) == 1.0
    #assert ranking_precision_score([1, 1, 0], [1, 0, 0.5], k=2) == 0.5
    #assert ranking_precision_score([1, 1, 0], [3, 2, 1], k=3) == ranking_precision_score([1, 1, 0], [1, 0, 0.5], k=3)

    # Average precision
    #from sklearn.metrics import average_precision_score as ap
    #assert average_precision_score([1, 1, 0], [3, 2, 1]) == ap([1, 1, 0], [3, 2, 1])
    #assert average_precision_score([1, 1, 0], [3, 1, 0]) == ap([1, 1, 0], [3, 1, 0])