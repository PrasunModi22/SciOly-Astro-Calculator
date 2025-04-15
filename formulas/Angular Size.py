import math

def solve(knowns):
    D = knowns.get("D") 
    d = knowns.get("d")
    theta = knowns.get("theta")

    if D is not None and d is not None:
        return {"theta": D / d}
    elif theta is not None and d is not None:
        return {"D": theta * d}
    elif theta is not None and D is not None:
        return {"d": D / theta}
    else:
        raise ValueError("Need two of the three values: D, d, theta")