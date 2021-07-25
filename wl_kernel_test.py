from collections import Counter
from wl_kernel import *


def test_init_labels(large_adjmatrix):
    res = {0: '3', 1: '4', 2: '2', 3: '2', 4: '2', 5: '3'}
    assert assign_init_labels(large_adjmatrix) == res


def test_determine_multisets(large_adjmatrix):
    labels = {0: '3', 1: '4', 2: '2', 3: '2', 4: '2', 5: '3'}
    res = {0: '3234', 1: '42233', 2: '233', 3: '224', 4: '224', 5: '3234'}
    assert determine_multisets(labels, large_adjmatrix) == res
    
    
def test_compression():
    labels = {0: '3234', 1: '42233', 2: '233', 3: '224', 4: '224', 5: '3234'}
    res = {
        0: '73d171a4a19b751918ee', 
        1: 'bd5f3292d9ae341d8c71', 
        2: 'be02d8b495ee9628bf36', 
        3: '369b457f4c1c75be4b80', 
        4: '369b457f4c1c75be4b80', 
        5: '73d171a4a19b751918ee'
    }
    assert compress_labels(labels) == res


def test_compute_graph_feature_vector():
    init_labels = Counter({0: '3', 1: '4', 2: '2', 3: '2', 4: '2', 5: '3'}.values())
    compressed = Counter({0: '2', 1: '2', 2: '3'}.values())
    v = compute_graph_feature_vector(init_labels, compressed)
    assert np.array_equal(v, [2, 1, 3, 2, 1])

