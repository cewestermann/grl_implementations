import numpy as np
import pytest

from traditional_methods import *
from utils import FLORENTINE_MATRIX


@pytest.mark.parametrize("idx, expected", [(0, 1), (1, 2), (2, 1)])
def test_node_degree(idx, expected, small_adjmatrix):
    assert node_degree(idx, small_adjmatrix) == expected


def test_node_centrality(large_adjmatrix):
    centralities = node_centrality(large_adjmatrix, iterations=30)
    assert np.allclose(centralities, np.array([0.47, 0.53, 0.33, 0.29, 0.29, 0.47]), atol=0.01)

