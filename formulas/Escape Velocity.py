import math

def solve(knowns):
    G = 6.67430e-11  
    M = knowns.get("M")
    r = knowns.get("r") 
    v = knowns.get("v")

    if M is not None and r is not None:
        return {"v": math.sqrt(2 * G * M / r)}
    elif v is not None and r is not None:
        return {"M": (v ** 2 * r) / (2 * G)}
    elif v is not None and M is not None:
        return {"r": (2 * G * M) / (v ** 2)}
    else:
        raise ValueError("Need two of the three values: M, r, v")
