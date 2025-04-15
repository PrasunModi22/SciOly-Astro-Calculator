def solve(knowns):
    b = 2.897771955e-3 
    T = knowns.get("T") 
    lambda_max = knowns.get("lambda_max") 

    if T is not None:
        return {"lambda_max": b / T}
    elif lambda_max is not None:
        return {"T": b / lambda_max}
    else:
        raise ValueError("Need one of the two values: T or lambda_max")
