import numpy as np


def adjmatrix_to_adjdict(matrix):

    def nonzero(array):
        return list(np.nonzero(array)[0])

    rows = range(len(matrix))
    indices = map(nonzero, matrix)
    return dict(zip(rows, indices))


def adjdict_to_adjmatrix(adjdict):

    def fill_matrix(matrix):
        for key, values in adjdict.items():
            for v in values:
                matrix[key, v] = 1.
        return matrix

    n_vertices = len(adjdict)
    matrix = np.zeros((n_vertices, n_vertices))
    return fill_matrix(matrix)


def neighbors(idx, matrix):
    return matrix[np.where(matrix[idx] == 1)[0]]


def cosine_similarity(v1, v2):
    nv1, nv2 = np.linalg.norm(v1), np.linalg.norm(v2)
    return (v1 @ v2) / (nv1 * nv2)



FLORENTINE_MATRIX = np.array([[0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [1., 0., 0., 0., 0., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0.],
                              [0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
                              [0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0.],
                              [0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0.],
                              [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0.],
                              [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
                              [0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 1.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.]]) 





