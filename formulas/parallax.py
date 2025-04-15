def solve(knowns):
    p = knowns.get("p") 
    d = knowns.get("d") 

    if p is not None:
        return {"d": 1 / p}
    elif d is not None:
        return {"p": 1 / d}
    else:
        raise ValueError("Need one of the two values: p or d")
