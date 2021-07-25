import numpy as np

from utils import *


def test_adjmatrix_to_adjdict():
    adjmatrix = np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])
    assert adjmatrix_to_adjdict(adjmatrix) == {0: [1], 1: [0, 2], 2: [1]}


def test_adjdict_to_adjmatrix():
    adjdict = {0: [1], 1: [0, 2], 2: [1]}
    assert np.array_equal(
            adjdict_to_adjmatrix(adjdict), np.array([[0, 1, 0],
                                                     [1, 0, 1],
                                                     [0, 1, 0]])
            )


def test_neighbors(large_adjmatrix):
    res = np.array([[1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0, 0]])
    assert np.array_equal(neighbors(0, large_adjmatrix), res)


def test_cosine_similarity():
    v1 = np.array([1, 2, 3])
    v2 = np.array([5, 2, 1])
    cs = cosine_similarity(v1, v2)
    assert np.isclose(cs, 0.586, rtol=1e-03)
