# AI Homework 3

The main purpose of this assignment was to implement Best-First, Uniform-Cost, and A-Star search algorithms given problems that can be reduced to a graph/tree involving states, actions, and a goal test for an end state.

*hw3_utils.py* was provided by the professor and contains the parent classes for Problem and Node.
*hw3.py* was the graded submission and contains the implementation for the search algorithms, as well as implementations for the N-Queens, Graph, and Eight Puzzle Problems.

Finding a solution for N-Queens:
```
queens_problem = NQueensProblem(8) #an 8x8 chess board
print(best_first_search(queens_problem).solution())
print(uniform_cost_search(queens_problem).solution())
print(a_star_search(queens_problem).solution())
```
The resulting array represents the zero-based index into a row for a particular column. For instance:
```
[2, 0, 3, 1]
```
represents a 4x4 board where there are Queens in the 2nd row of the 0th column, the 0th row of the 1st column, the 3rd row of the 2nd column, and the 1st row of the 3rd column.

The heuristic for N-Queens is represented as the total number of conflicts presently on the board. For instance, a board with:
`[0, 1, 3, 2]`
will have a heuristic value of 3 as there are 3 unique conflicts.
