# Practical 1

## Ideas of electronics

### Interlude: review of logic

#### Exercise: Compute the truth table for NOT:

X | NOT X
--|-------
0 |   1
1 |   0

#### Exercise: Compute the truth table table for AND.

X | Y | X AND Y
--|---|--------
0 | 0 |   0
0 | 1 |   0
1 | 0 |   0
1 | 1 |   1

#### Exercise: Compute the truth table for exclusive-or, defined by the formula:

XOR(X, Y) = (X OR Y) AND NOT (X AND Y)

X | Y | A = X AND Y | B = X OR Y | NOT A | XOR(X, Y)
--|---|-------------|------------|-------|-----------
0 | 0 |      0      |      0     |   1   |     0
0 | 1 |      0      |      1     |   1   |     1
1 | 0 |      0      |      1     |   1   |     1
1 | 1 |      1      |      1     |   0   |     0

#### Exercise: Prove De Morgan's theorem, NOT(X OR Y) = NOT(X) AND NOT(Y), by completing the table and checking the last two columns are the same.

X | Y | A = X OR Y | B = NOT X | C = NOT Y | NOT A | B AND C
--|---|------------|-----------|-----------|-------|---------
0 | 0 |      0     |     1     |     1     |   1   |    1
0 | 1 |      1     |     1     |     0     |   0   |    0
1 | 0 |      1     |     0     |     1     |   0   |    0
1 | 1 |      1     |     0     |     0     |   0   |    0

#### Exercise: using truth tables, check these three equations

NOT(X) = NAND(1, X) = NOT(1 AND X)
AND(X, Y) = NOT(NAND(X, Y)) = NOT(NOT(X AND Y))
OR(X, Y) = NAND(NOT(X), NOT(Y))) = NOT(NOT(X) AND NOT(Y))

X | Y | NOT(X) | A = 1 AND X | NOT A = NAND(1, X)
--|---|--------|-------------|-------------------
0 | 0 |    1   |       0     |         1
0 | 1 |    1   |       0     |         1
1 | 0 |    0   |       1     |         0
1 | 1 |    0   |       1     |         0

X | Y | A = X AND Y | B = NOT A | NOT B = NOT(NAND(X, Y))
--|---|-------------|-----------|------------------------
0 | 0 |      0      |     1     |           0
0 | 1 |      0      |     1     |           0
1 | 0 |      0      |     1     |           0
1 | 1 |      1      |     0     |           1

X | Y | A = NOT X | B = NOT Y | C = A AND B | NOT C = NAND(NOT(X), NOT(Y))) | X OR Y
--|---|-----------|-----------|-------------|-------------------------------|--------
0 | 0 |     1     |     1     |      1      |                0              |   0
0 | 1 |     1     |     0     |      0      |                1              |   1
1 | 0 |     0     |     1     |      0      |                1              |   1
1 | 1 |     0     |     0     |      0      |                1              |   1

#### Exercise: write similar formulas expressing NOT, AND, and OR in terms of NOR

NOT(X) = NOR(0,X)
AND(X,Y) = NOR(NOT(X),NOT(Y)))
OR(X,Y) = NOT(NOR(X,Y))