def modus_ponens(p, implication):
    
    # 
    if isinstance(implication, tuple) and len(implication) == 2:
        p_imp, q = implication
        # If P is true and implication is of the form "P -> Q", return Q
        if p == p_imp:
            return q
    return None  # If Modus Ponens can't be applied

# Example usage
P = True  # Assume P is true
Q = "It is raining"
implication = (True, Q)  # This represents "If P, then Q"

result = modus_ponens(P, implication)

if result:
    print("Conclusion:", result)
else:
    print("Modus Ponens cannot be applied.")
    
#modus tollens
def modus_tollens(q, implication):
    # Check if the implication is in the form of "P -> Q"
    if isinstance(implication, tuple) and len(implication) == 2:
        p, q_imp = implication
        # If Q is false and implication is of the form "P -> Q", return not P
        if q == q_imp:
            return not p
    return None  # If Modus Tollens can't be applied

# Example usage
Q = False  # Assume Q is false
P = True   # Assume P is true
implication = (P, True)  # This represents "If P, then Q"

result = modus_tollens(Q, implication)

if result is not None:
    print("Conclusion: P is", not result)  # negation of the returned value
else:
    print("Modus Tollens cannot be applied.")
#
def hypothetical_syllogism(p_q, q_r):
    # Check if the implications are valid
    if isinstance(p_q, tuple) and isinstance(q_r, tuple) and len(p_q) == 2 and len(q_r) == 2:
        p, q = p_q
        q2, r = q_r
        # If Q is the same in both implications, return the new implication P -> R
        if q == q2:
            return (p, r)
    return None  # If Hypothetical Syllogism can't be applied

# Example usage
p_q = (True, "B")  # If P, then Q ("If it rains, then the ground is wet")
q_r = ("B", "C")   # If Q, then R ("If the ground is wet, then it is muddy")

result = hypothetical_syllogism(p_q, q_r)

if result:
    print("Conclusion: If P, then R")
else:
    print("Hypothetical Syllogism cannot be applied.")
#
def disjunctive_syllogism(p_or_q, not_p):
    # Check if the disjunction is valid
    if isinstance(p_or_q, tuple) and len(p_or_q) == 2:
        p, q = p_or_q
        # If P is false, return Q
        if not_p == p:
            return q
    return None  # If Disjunctive Syllogism can't be applied

# Example usage
p_or_q = (False, "It is sunny")  # Either P (it is raining) or Q (it is sunny)
not_p = False  # Assume P is false (it is not raining)

result = disjunctive_syllogism(p_or_q, not_p)

if result is not None:
    print("Conclusion:", result)
else:
    print("Disjunctive Syllogism cannot be applied.")
#
def simplification(p_and_q):
    # Check if the input is a conjunction of P and Q
    if isinstance(p_and_q, tuple) and len(p_and_q) == 2:
        p, q = p_and_q
        # Return both P and Q
        return p, q
    return None  # If simplification can't be applied

# Example usage
P = True     # Assume P is true
Q = "It is raining"  # Assume Q is also true
p_and_q = (P, Q)  # This represents "P and Q"

result = simplification(p_and_q)

if result:
    print("Conclusion: P is", result[0], "and Q is", result[1])
else:
    print("Simplification cannot be applied.")
#
def resolution(clause1, clause2):
    # Check if the clauses are valid
    if isinstance(clause1, tuple) and isinstance(clause2, tuple):
        # Extract propositions
        p, q = clause1  # Clause 1 (P or Q)
        not_p, r = clause2  # Clause 2 (not P or R)

        # Check if the first proposition of clause1 is negated in clause2
        if p == not_p:
            return (q, r)  # Return the resolved clause (Q or R)
    return None  # If resolution can't be applied

# Example usage
clause1 = (True, "It is sunny")  # P or Q
clause2 = (False, "It is raining")  # not P or R

result = resolution(clause1, clause2)

if result:
    print("Conclusion: Either", result[0], "or", result[1], "is true.")
else:
    print("Resolution cannot be applied.")

