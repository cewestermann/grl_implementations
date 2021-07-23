import pytest
import numpy as np


@pytest.fixture(scope='module')
def small_adjmatrix():
    return np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])


@pytest.fixture(scope='module')
def large_adjmatrix():
    return np.array([
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0]
    ])


@pytest.fixture(scope='module')
def small_adjdict():
    return {0: [1], 1: [0, 2], 2: [1]}


@pytest.fixture(scope='module')
def large_adjdict():
    return {
        0: [1, 2, 5],
        1: [0, 3, 4, 5],
        2: [0, 5],
        3: [1, 4],
        4: [1, 3],
        5: [0, 1, 2]
    }
