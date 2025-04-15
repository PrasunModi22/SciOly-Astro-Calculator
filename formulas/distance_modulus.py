import math

def solve(knowns):
    m = knowns.get("m") 
    M = knowns.get("M") 
    d = knowns.get("d") 

    if m is not None and M is not None:
        return {"d": 10 ** ((m - M + 5) / 5)}
    elif m is not None and d is not None:
        return {"M": m - 5 * math.log10(d) + 5}
    elif M is not None and d is not None:
        return {"m": M + 5 * math.log10(d) - 5}
    else:
        raise ValueError("Need two of the three values: m, M, d")