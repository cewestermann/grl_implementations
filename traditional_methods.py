import numpy as np

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


