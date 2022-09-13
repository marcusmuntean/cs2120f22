# Marcus Muntean - xhm3ws
from z3 import Bool, And, Or, Not, Solver
from itertools import combinations

def at_most_one(literals):
    c = []
    a=0
    b=1
    for pair in combinations(literals, 2):
        c += [Or(Not(pair[a]), Not(pair[b]))]
    return And(c)

x = [[Bool("x_%i_%i" % (i, j)) for j in range(5)] for i in range(5)]

s = Solver()

for i in range(5):
    s.add(Or(x[i]))

for i in range(5):
    col = []
    for j in range(5):
        col += [x[j][i]]
    s.add(at_most_one(x[i]))
    s.add(at_most_one(col))


for i in range(4):
    diag_1 = []
    diag_2 = []
    diag_3 = []
    diag_4 = []
    for j in range(5 - i):
        diag_1 += [x[i+j][j]]
        diag_2 += [x[4-(i+j)][j]]
        diag_3 += [x[i+j][4-j]]
        diag_4 += [x[4-(i+j)][4-j]]
    s.add(at_most_one(diag_1))
    s.add(at_most_one(diag_2))
    s.add(at_most_one(diag_3))
    s.add(at_most_one(diag_4))

s.check()

m = s.model()

for i in range(5):
    line = ""
    for j in range(5):
        if m.evaluate(x[i][j]):
            line += "x "
        else:
            line += ". "
    print(line)