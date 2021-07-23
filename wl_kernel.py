import string
import numpy as np

from hashlib import blake2b

from traditional_methods import node_degree
from utils import adjmatrix_to_adjdict, adjdict_to_adjmatrix, neighbors


G = np.array([
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1]
])


def assign_init_labels(adjmatrix):
    return {i: str(node_degree(i, adjmatrix)) for i, n in zip(range(len(adjmatrix)), adjmatrix)}


def determine_multisets(labels, adjmatrix):
    new_labels = dict()

    adjdict = adjmatrix_to_adjdict(adjmatrix)
    for node, label in labels.items():
        nbors = adjdict[node]
        multiset = [labels[nbor] for nbor in nbors]
        new_labels[node] = label + ''.join(sorted(multiset))
    return new_labels


def compress_labels(labels):
    new_labels = dict()

    for node, label in labels.items():
        h = blake2b(digest_size=10)
        h.update(str.encode(label))
        new_labels[node] = h.hexdigest()
    return new_labels









