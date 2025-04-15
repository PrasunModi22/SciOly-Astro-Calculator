import math

def solve(knowns):
    sigma = 5.670374419e-8  
    R = knowns.get("R")  
    T = knowns.get("T") 
    L = knowns.get("L")  

    if R is not None and T is not None:
        return {"L": 4 * math.pi * R ** 2 * sigma * T ** 4}
    elif L is not None and T is not None:
        return {"R": math.sqrt(L / (4 * math.pi * sigma * T ** 4))}
    elif L is not None and R is not None:
        return {"T": (L / (4 * math.pi * R ** 2 * sigma)) ** 0.25}
    else:
        raise ValueError("Need two of the three values: R, T, L")
