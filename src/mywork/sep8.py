from z3 import *

T = Real('T')
C = Real('C')
S = Real('S')

C1 = (T+S+C==10)
C2 = (C+S-T==6)
C3 = (C+T-S==4)

C = And(C1, C2, C3)
s = Solver()
s.add(C)
isSat = s.check()
if (isSat == sat):
    print(s.model())
else:
    print("No solution")
