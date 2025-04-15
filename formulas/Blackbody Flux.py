import math

def solve(knowns):
    sigma = 5.670374419e-8  
    T = knowns.get("T") 
    F = knowns.get("F")

    if T is not None:
        return {"F": sigma * T ** 4}
    elif F is not None:
        return {"T": (F / sigma) ** 0.25}
    else:
        raise ValueError("Need one of the two values: T or F")