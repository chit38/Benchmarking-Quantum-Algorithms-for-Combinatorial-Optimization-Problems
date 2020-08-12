def using_numpyeigensolver(n, adj_matrix):
    qubitop, offset = max_cut.get_operator(adj_matrix)
    qudratic = IsingToQuadraticProgram()
    qudratic_problem = qudratic.encode(qubitop, offset)
    solver = MinimumEigenOptimizer(NumPyMinimumEigensolver())
    result = solver.solve(qudratic_problem)
    best_cost = float(str(result).split('-')[1])
    return best_cost