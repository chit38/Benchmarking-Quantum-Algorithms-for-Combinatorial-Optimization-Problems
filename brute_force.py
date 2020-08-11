import numpy as np
import random
def brute_force(n, adj_matrix):
    best_cost = 0
    best_x = None
    for k in range(2**n):
        x=dec_to_bin(k)
        temp_cost = 0
        for i in range(n):
            for j in range(n):
                temp_cost = temp_cost + adj_matrix[i,j]*x[i]*(1-x[j])
        if temp_cost > best_cost:
            best_cost = temp_cost
            best_x = x
        print(binary_k)

brute_force(3,np.zeros((3,3)))