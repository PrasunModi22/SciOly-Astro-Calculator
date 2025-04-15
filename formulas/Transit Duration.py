import math

def solve(knowns):
    P = knowns.get("P")
    a = knowns.get("a") 
    R = knowns.get("R") 
    T = knowns.get("T")  

    if P is not None and a is not None and R is not None:
        return {"T": (P * R) / (math.pi * a)}
    elif T is not None and a is not None and R is not None:
        return {"P": (T * math.pi * a) / R}
    elif T is not None and P is not None and R is not None:
        return {"a": (P * R) / (math.pi * T)}
    elif T is not None and P is not None and a is not None:
        return {"R": (T * math.pi * a) / P}
    else:
        raise ValueError("Need three of the four values: P, a, R, T")