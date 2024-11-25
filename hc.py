from pysmt.shortcuts import Symbol, And, Or, Solver, ExactlyOne, Not
from pysmt.typing import BOOL


def hamiltonian_cycle_sat(nodes, edges):
    constraints = []
    positions = range(len(nodes))
    # Put Your Code Here #
    vars = {(v, pos): Symbol(f"v({v}_{pos})", BOOL) for v in nodes for pos
            in positions}
    # check that vertx appears in just one position
    for v in nodes:
        constraints.append(ExactlyOne(vars[v, pos] for pos in positions))

    # check that every pos contains single node
    for pos in positions:
        constraints.append(ExactlyOne(vars[v, pos] for v in nodes))

    #Only valid edges can connect consecutive nodes in the cycle
    for pos in positions:
        next_pos = (pos + 1) % len(positions)  # Wrap around for the last position
        for node1 in nodes:
            for node2 in nodes:
                if (node1, node2) not in edges and (node2, node1) not in edges:
                    constraints.append(Or(Not(vars[(node1, pos)]), Not(vars[(node2, next_pos)])))  # Invalid edge constraint

    # Combine all constraints
    formula = And(constraints)

    # Solve with a SAT solver
    with Solver(name="z3") as solver:
        solver.add_assertion(formula)
        if solver.solve():
            # If satisfiable, extract solution
            cycle = [None] * len(nodes)
            for pos in range(len(nodes)):
                for node in nodes:
                    if solver.get_value(vars[(node, pos)]).is_true():
                        cycle[pos] = node
            return cycle
        else:
            return None


# Example usage
# nodes = ["A", "B", "C", "D"]
# edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("B", "D")]


# Example presentation"""
nodes = [x + 1 for x in range(20)]
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
