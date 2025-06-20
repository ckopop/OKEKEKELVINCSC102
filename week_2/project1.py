#cubic equation solver
A = float(input("value of A: "))
B = float(input("value of B: "))
C = float(input("value of C: "))
D = float(input("value of D: "))
import numpy as np

def find_cubic_roots(a, b, c, d):
    if a == 0:
        print("Not a cubic equation.")
        return
    
    roots = np.roots([a, b, c, d])
    print("Roots:", roots)
    
    return roots
find_cubic_roots(A, B, C, D)
