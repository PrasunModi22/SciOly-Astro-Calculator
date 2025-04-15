def solve(knowns):
    a = knowns.get("a") 
    P = knowns.get("P") 

    if a is not None:
        return {"P": a ** 1.5}
    elif P is not None:
        return {"a": P ** (2/3)}
    else:
        raise ValueError("Need one of the two values: a or P")
