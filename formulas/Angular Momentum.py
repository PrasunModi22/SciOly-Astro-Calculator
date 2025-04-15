def solve(knowns):
    m = knowns.get("m")  
    v = knowns.get("v") 
    r = knowns.get("r")
    L = knowns.get("L")

    if m is not None and v is not None and r is not None:
        return {"L": m * v * r}
    elif L is not None and v is not None and r is not None:
        return {"m": L / (v * r)}
    elif L is not None and m is not None and r is not None:
        return {"v": L / (m * r)}
    elif L is not None and m is not None and v is not None:
        return {"r": L / (m * v)}
    else:
        raise ValueError("Need three of the four values: m, v, r, L")
