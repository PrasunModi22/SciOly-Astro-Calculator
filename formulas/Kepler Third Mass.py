import math

def solve(knowns):
    G = 6.67430e-11  
    M = knowns.get("M") 
    r = knowns.get("r") 
    P = knowns.get("P") 

    if M is not None and r is not None:
        return {"P": 2 * math.pi * math.sqrt(r ** 3 / (G * M))}
    elif P is not None and r is not None:
        return {"M": (4 * math.pi ** 2 * r ** 3) / (G * P ** 2)}
    elif P is not None and M is not None:
        return {"r": ((G * M * P ** 2) / (4 * math.pi ** 2)) ** (1/3)}
    else:
        raise ValueError("Need two of the three values: M, r, P")
