# PigeonholePrinciple
This python program takes as input n, and uses z3 SAT solver
 to proof that if there are n pigeons living in n-1 nests, 
 then at least one nest must contain two or more pigeons.

The propoistional logic formula used is:
 ∀i, j, k, l  (((j ≠ k) ∧ (j, k ≤ n-1)) → (X_{i,j} → ¬X_{i,k})) 
 ∧ (((i ≠ l) ∧ (i, l ≤ n)) → (X_{i,j} → ¬X_{l,j}))
 ∀i, ∃j X_{i,j} 

If the Pigeonhole Princpile holds, the SAT solver must return 
Unsatisfiable.

Side observations:
- Test: when number of pigeons = nests -> SAT solver returns 
Satisfiable and finds an assignmenet where each Pigeon is in 
one nest.
- My personal computer can hold up to n = 13, for which it 
needs 3 minutes and 40 seconds, however, n = 5 is solved in 
0.01 seconds.
