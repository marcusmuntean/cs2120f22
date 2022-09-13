from z3 import *

def hw2():
    X, Y, Z = Bools('X Y Z')
    s= Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y
    # As proposition: ((X \/ Y) /\ X) -> ~Y
    # In english: If X Or Y is true, and if X is true, then Y must not be true
    C1 = Implies((And(Or(X, Y), X)), Not(Y))
    s.add(Not(C1))
    # I believe it's not valid
    r = s.check()
    
    if (r == unsat):
        print("C1 is valid")
    else:
        print("C1 is not valid. Here's a counter-example ", s.model())
    # Why doesn't make sense in English: If X or Y is true and If X is true, it is
    # still possible that Y is true (X or Y is still true in this case). Therefore, it is
    # wrong to conclude that Y is false in every case, making this not valid.
    
    
    
    
    # 2. X, Y ⊢ X ∧ Y
    # As proposition: (X) /\ (Y) -> (X /\ Y)
    # In english: If X is true, and if Y is true, then X And Y must be true
    C2 = Implies(And(X, Y), And(X, Y))
    s.reset()
    s.add(Not(C2))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C2 is valid")
    else:
        print("C2 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 3. X ∧ Y ⊢ X 
    # As proposition: (X /\ Y) -> X
    # In english: If X And Y is true, then X must be true
    C3 = Implies(And(X, Y), X)
    s.reset()
    s.add(Not(C3))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C3 is valid")
    else:
        print("C3 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 4. X ∧ Y ⊢ Y
    # As proposition: (X /\ Y) -> Y
    # In english: If X And Y is true, then Y must be true
    C4 = Implies(And(X, Y), Y)
    s.reset()
    s.add(Not(C4))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C4 is valid")
    else:
        print("C4 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 5. ¬¬X ⊢ X
    # As proposition: ~~X -> X
    # In english: If Not Not X is true, then X must be true
    C5 = Implies(Not(Not(X)), X)
    s.reset()
    s.add(Not(C5))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C5 is valid")
    else:
        print("C5 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 6. ¬(X ∧ ¬X)
    # As proposition: ~(X /\ ~X)
    # In english: The opposite of X And Not X
    C6 = Not(And(X, Not(X)))
    s.reset()
    s.add(Not(C6))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C6 is valid")
    else:
        print("C6 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 7. X ⊢ X ∨ Y 
    # As proposition: X -> X \/ Y
    # In english: If X is true, then X Or Y must be true
    C7 = Implies(X, Or(X, Y))
    s.reset()
    s.add(Not(C7))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C7 is valid")
    else:
        print("C7 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 8. Y ⊢ X ∨ Y
    # As proposition: Y -> X \/ Y
    # In english: If Y is true, then X Or Y must be true
    C8 = Implies(Y, Or(X, Y))
    s.reset()
    s.add(Not(C8))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C8 is valid")
    else:
        print("C8 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 9. X → Y, ¬X ⊢ ¬ Y
    # As proposition: ((X -> Y) /\ ~X) -> ~Y
    # In english: If X Implies Y is true, and if Not X is true, then Not Y must be true
    C9 = Implies(And(Implies(X, Y), Not(X)), Not(Y))
    s.reset()
    s.add(Not(C9))
    # I believe it's not valid
    r = s.check()
    
    if (r == unsat):
        print("C9 is valid")
    else:
        print("C9 is not valid. Here's a counter-example ", s.model())
    # Why doesn't make sense in English: When X is false and Y is true, X -> Y is
    # true, and Not X is true, (making the setup true) but Not Y is false (since Y is true). This shows that Number 9 on the
    # homework is not valid (it's not true in every interpretation).
    
    
    
    
    # 10. X → Y, Y → X ⊢ X ↔ Y
    # As proposition: ((X -> Y) /\ (Y → X)) -> (X ↔ Y)
    # In english: If X Implies Y is true, and if Y Implies X is true, then X and Y must be equivalent
    C10 = Implies(And(Implies(X, Y), Implies(Y, X)), X == Y)
    s.reset()
    s.add(Not(C10))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C10 is valid")
    else:
        print("C10 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 11. X ↔ Y ⊢ X → Y
    # As proposition: (X ↔ Y) -> (X -> Y)
    # In english: If X is equivalent to Y is true, then X must Imply Y
    C11 = Implies(X == Y, Implies(X, Y))
    s.reset()
    s.add(Not(C11))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C11 is valid")
    else:
        print("C11 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 12. X ↔ Y ⊢ Y → X
    # As proposition: (X ↔ Y) -> (Y -> X)
    # In english: If X is equivalent to Y is true, then Y must Imply X
    C12 = Implies(X == Y, Implies(Y, X))
    s.reset()
    s.add(Not(C12))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C12 is valid")
    else:
        print("C12 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 13. X ∨ Y, X → Z, Y → Z ⊢ Z
    # As proposition: (X \/ Y) /\ (X -> Z) /\ (Y -> Z) -> Z
    # In english: If X Or Y is true, and X Implies Z, and Y Implies Z, then Z must be true
    C13 = Implies(And(And(Or(X, Y), Implies(X, Z)), Implies(Y, Z)), Z)
    s.reset()
    s.add(Not(C13))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C13 is valid")
    else:
        print("C13 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 14. X → Y, Y ⊢ X
    # As proposition: (X -> Y) /\ (Y) -> X
    # In english: If X Implies Y is true, and Y is true, then X must be true
    C14 = Implies(And(Implies(X, Y), Y), X)
    s.reset()
    s.add(Not(C14))
    # I believe it's not valid
    r = s.check()
    
    if (r == unsat):
        print("C14 is valid")
    else:
        print("C14 is not valid. Here's a counter-example ", s.model())
    # Why doesn't make sense in English: When X is false and Y is true, X -> Y is
    # true, and Y is true (making the setup true), but X is false. This shows that Number 14 on the
    # homework is not valid (it's not true in every interpretation).
    
    
    
    
    # 15. X → Y, X ⊢ Y
    # As proposition: (X -> Y) /\ (X) -> Y
    # In english: If X Implies Y is true, and X is true, then Y must be true
    C15 = Implies(And(Implies(X, Y), X), Y)
    s.reset()
    s.add(Not(C15))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C15 is valid")
    else:
        print("C15 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 16. X → Y, Y → Z ⊢ X → Z
    # As proposition: (X -> Y) /\ (Y -> Z) -> (X -> Z)
    # In english: If X Implies Y is true, and Y Implies Z is true, then X must Imply Z
    C16 = Implies(And(Implies(X, Y), Implies(Y, Z)), Implies(X, Z))
    s.reset()
    s.add(Not(C16))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C16 is valid")
    else:
        print("C16 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 17. X → Y ⊢ Y → X 
    # As proposition: (X -> Y) -> (Y -> X)
    # In english: If X Implies Y is true, then Y must Imply X
    C17 = Implies(Implies(X, Y), Implies(Y, X))
    s.reset()
    s.add(Not(C17))
    # I believe it's not valid
    r = s.check()
    
    if (r == unsat):
        print("C17 is valid")
    else:
        print("C17 is not valid. Here's a counter-example ", s.model())
    # Why doesn't make sense in English: When X is false and Y is true, X -> Y is
    # true, but Y -> X is false. This shows that Number 17 on the
    # homework is not valid (it's not true in every interpretation).
    
    
    
    
    # 18. X → Y ⊢ ¬Y → ¬X 
    # As proposition: (X -> Y) -> (~Y -> ~X)
    # In english: If X Implies Y is true, then Not Y must Imply Not X
    C18 = Implies(Implies(X, Y), Implies(Not(Y), Not(X)))
    s.reset()
    s.add(Not(C18))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C18 is valid")
    else:
        print("C18 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y
    # As proposition: ~(X \/ Y) ↔ (~X /\ ~Y)
    # In english: If X Or Y is not true, then Not X And Not Y is equivalent to Not (X or Y)
    C19 = Not(Or(X, Y)) == And(Not(X), Not(Y))
    s.reset()
    s.add(Not(C19))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C19 is valid")
    else:
        print("C19 is not valid. Here's a counter-example ", s.model())
    
    
    
    
    # 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y
    # As proposition: ~(X /\ Y) ↔ (~X \/ ~Y)
    # In english: If X And Y is not true, then Not X Or Not Y is equivalent to Not (X and Y)
    C20 = Not(And(X, Y)) == Or(Not(X), Not(Y))
    s.reset()
    s.add(Not(C20))
    # I believe it's valid
    r = s.check()
    
    if (r == unsat):
        print("C20 is valid")
    else:
        print("C20 is not valid. Here's a counter-example ", s.model())


hw2()