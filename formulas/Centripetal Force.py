def solve(knowns):
    m = knowns.get("m") 
    v = knowns.get("v") 
    r = knowns.get("r")  
    Fc = knowns.get("Fc")  

    if m is not None and v is not None and r is not None:
        return {"Fc": m * v ** 2 / r}
    elif Fc is not None and v is not None and r is not None:
        return {"m": Fc * r / v ** 2}
    elif Fc is not None and m is not None and v is not None:
        return {"r": m * v ** 2 / Fc}
    elif Fc is not None and m is not None and r is not None:
        return {"v": (Fc * r / m) ** 0.5}
    else:
        raise ValueError("Need three of the four values: m, v, r, Fc")