import math

def solve(knowns):
    G = 6.67430e-11  
    M = knowns.get("M") 
    r = knowns.get("r") 
    g = knowns.get("g") 

    if M is not None and r is not None:
        return {"g": G * M / r ** 2}
    elif g is not None and r is not None:
        return {"M": g * r ** 2 / G}
    elif g is not None and M is not None:
        return {"r": math.sqrt(G * M / g)}
    else:
        raise ValueError("Need two of the three values: M, r, g")