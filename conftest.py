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



