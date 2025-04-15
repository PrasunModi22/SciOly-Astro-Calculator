def solve(knowns):
    H0 = 70
    v = knowns.get("v")   
    d = knowns.get("d") 

    if v is not None:
        return {"d": v / H0}
    elif d is not None:
        return {"v": H0 * d}
    else:
        raise ValueError("Need one of the two values: v or d")