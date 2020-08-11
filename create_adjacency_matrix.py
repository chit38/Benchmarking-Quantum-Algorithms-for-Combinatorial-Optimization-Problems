import numpy as np
import random
def create_adjacency_matrix(number_of_vertices, probability):
    adj_matrix = np.ones((number_of_vertices,number_of_vertices))
    for i in range(0,number_of_vertices):
        for j in range(0,number_of_vertices):
            if random.random()>probability:
                adj_matrix[i][j]=0
    return print(adj_matrix)

create_adjacency_matrix(20,0.5)