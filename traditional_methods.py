import numpy as np
import itertools

from utils import adjmatrix_to_adjdict


def node_degree(idx, adjmatrix):
    '''
    Number of edges attached to node at idx.
    Since the graph is undirected, the adjacency matrix is symmetric and you could
    double the number of edges (i.e., each edge points both ways) but I stick to just
    counting each edge once. 
    '''
    d = adjmatrix_to_adjdict(adjmatrix)
    return len(d[idx])


def node_centrality(adjmatrix, iterations=30):
    '''
    Eigenvector centrality. A property of the adjacency matrix is that if you raise it 
    to the nth power, the result will be a matrix showing the number of length n paths
    that connects each node. 

    The dominant eigenvector (the eigenvector attached to the largest eigenvalue) can be 
    found using power iteration which I perform below. 

    We normalize at each iteration and you can interpret the output as being the
    likelihood of a given node being visited during an infinite random walk.

    It is a recurrence relation, so it just made sense to implement it recursively.
    '''
    # Initialize eigenvector to random values
    e = np.random.rand(adjmatrix.shape[0])

    def helper(eigv, iterations):
        if not iterations:
            return eigv
        e_t = adjmatrix @ eigv
        norm = np.linalg.norm(e_t)
        eigv = e_t / norm
        return helper(eigv, iterations-1)
    
    return helper(e, iterations)


def clustering_coefficient(idx, adjmatrix):
    '''
    Clustering coefficient, i.e., the ratio of closed triangles in the ego-network
    of node at idx. If there are three possible closed triangles out of a possible four,
    the clustering coefficient will yield 0.75.
    '''
    # TODO: Could be made way simpler using adjdict. 
    
    def n_choose2(n):
        return len(list(itertools.permutations(n, 2)))

    node = adjmatrix[idx]
    idxes = np.where(node == 1)[0]
    neighbors = adjmatrix[idxes]

    count = 0
    for row in neighbors:
        count += sum(x for i, x in enumerate(row) if i in idxes)
    return round(count / n_choose2(idxes), 2)





