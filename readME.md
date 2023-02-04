# Super N-Queens and 5 Tree Search Algorithms
Written By Ian McKechnie
For CIS*3700: Intro To Inteligent Systems
At The University Of Guelph
Feb 3rd, 2023

## Tree Search Algorithms
Run with `python3 treeSearches.py`

It will print the path it searched to find the node F

Output should look like this:
```
Depth First Search
S-A-G-E-F-F
Breadth First Search
S-A-C-B-G-H-D-E-F
Uniform cost search
S-B-A-G-D-F
Greedy Best-First Searhc
S-C-H-D-F
A* Search
S-A-G-E-F
```

## Super Queens
Run with `python3 superQueens.py`

Super Queens is like the N-Queens problem but Queens can also move in the same way as a Knight (In an L shape) so the goal is to MINIMIZE colisions between Queens.

It will promp you for N, which is used to define the board size at NxN, then find the optimal placement of Queens on the board.