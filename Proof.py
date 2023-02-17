import time
from z3 import *

n = 5 # Number of pigeons and pigeonholes
m = n-1

# Declare boolean variables for each pigeonhole and pigeon combination
# Xij = true implies that pigeon i is in nest j.
X = [[Bool(f"X_{i}_{j}") for j in range(m)] for i in range(n)]

# Create a Z3 solver instance
solver = Solver()

# Add the formula to the solver
for i in range(n):
    for j in range(m):
        for k in range(m):
            if j != k:
                # Constrain: each pigeon can only be in at most one nest
                solver.add(Implies(X[i][j], Not(X[i][k]))) 
                solver.add(Implies(X[i][k], Not(X[i][j])))

        for l in range(n):
            if i != l:
                # Constrain: each nest has at most one pigeon
                solver.add(Implies(X[i][j], Not(X[l][j])))
                solver.add(Implies(X[l][j], Not(X[i][j])))

# Constrain: every pigeon be must be in minumum one nest
for i in range(n):
    # Create a list of variables for the ith row
    row_vars = [X[i][j] for j in range(m)]
    # Add a clause that asserts that at least one variable in the ith row is true
    solver.add(Or(row_vars))

# Start time
start_time = time.time()

# Check if the formula is satisfiable
result = solver.check()

# End time
end_time = time.time()

# Compute elapsed time
elapsed_time = end_time - start_time

# Print variable results if SAT
if result == sat:
    print("SAT")
    model = solver.model()
    for i in range(n):
        for j in range(m):
            if is_true(model.eval(X[i][j])):
                print(f"Pigeon {i} is in nest {j}")
# EXPECTED: UNSAT
else:
    print("UNSAT")

# Print elapsed time
print(f"Program took {elapsed_time:.2f} seconds to terminate")