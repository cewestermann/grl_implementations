import string
import numpy as np

from hashlib import blake2b
from collections import Counter

from traditional_methods import node_degree
from utils import adjmatrix_to_adjdict, adjdict_to_adjmatrix, neighbors


def assign_init_labels(adjmatrix):

    def _node_idxes(): return range(len(adjmatrix))

    return {i: str(node_degree(i, adjmatrix)) for i, n in zip(_node_idxes(), adjmatrix)}


def determine_multisets(labels, adjmatrix):
    new_labels = dict()

    adjdict = adjmatrix_to_adjdict(adjmatrix)
    for node, label in labels.items():
        nbors = adjdict[node]
        multiset = [labels[nbor] for nbor in nbors]
        new_labels[node] = label + ''.join(sorted(multiset))
    return new_labels


def compress_labels(labels):

    def _hash(label):
        h = blake2b(digest_size=10)
        h.update(str.encode(label))
        return h.hexdigest()

    new_labels = dict()

    for node, label in labels.items():
        new_labels[node] = _hash(label)
    return new_labels


def compute_graph_feature_vector(init, compressed):
    return np.array([*init.values(), *compressed.values()])


def weisfeiler_lehman(adjmatrix, iterations=3):
    init = assign_init_labels(adjmatrix)
    for i in range(iterations):
        c_init = Counter(init.values())
        multisets = determine_multisets(init, adjmatrix)
        compressed = compress_labels(multisets)
        c_compressed = Counter(compressed.values())
        f_vector = compute_graph_feature_vector(c_init, c_compressed)


