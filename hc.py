from pysmt.shortcuts import Symbol, And, Or, Not, Solver
from pysmt.typing import BOOL
import random

def hamiltonian_cycle_sat(nodes, edges):
    constraints = []

    # Put Your Code Here #

    # Combine all constraints
    formula = And(constraints)

    # Solve with a SAT solver
    with Solver(name="z3") as solver:
        solver.add_assertion(formula)
        if solver.solve():
            # If satisfiable, extract solution
            cycle = [None] * n
            for pos in range(n):
                for node in nodes:
                    if solver.get_value(vars[(node, pos)]).is_true():
                        cycle[pos] = node
            return cycle
        else:
            return None

# Example usage
# nodes = ["A", "B", "C", "D"]
# edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("B", "D")]


# Example presentation
nodes = [x+1 for x in range(20)]
edges = [(1, 20), (1, 2), (1, 5),
         (2, 18), (2, 3),
         (3, 4), (3, 16),
         (4, 5), (4, 14),
         (5, 6),
         (6, 7), (6, 13),
         (7, 8), (7, 20),
         (8, 9), (8, 12),
         (9, 19), (9, 10),
         (10, 17), (10, 11),
         (11, 12), (11, 15),
         (12, 13),
         (13, 14),
         (14, 15),
         (15, 16),
         (17, 18),
         (18, 19),
         (19, 20)]

# BIG Example
# def generate_random_pairs(num_pairs,n):
#     pairs = [(random.randint(0, n-1), random.randint(0, n-1)) for _ in range(num_pairs)]
#     pairs = set(pairs)
#     pairs = [(x1,x2) for (x1,x2) in pairs if x1 != x2]
#     return pairs
#
# n = 50
# num_pairs = 450
# nodes = [x for x in range(n)]
# edges = set(generate_random_pairs(num_pairs, n))

solution = hamiltonian_cycle_sat(nodes, edges)
if solution:
    print("Hamiltonian Cycle found:")
    for v in solution:
        print(f'{v} -> ', end='')
    print(solution[0])
else:
    print("No Hamiltonian Cycle exists.")