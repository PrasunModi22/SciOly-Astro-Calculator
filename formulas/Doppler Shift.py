def solve(knowns):
    c = 3e8  
    delta_lambda = knowns.get("delta_lambda")  
    lambda_0 = knowns.get("lambda_0")       
    v = knowns.get("v")   

    if delta_lambda is not None and lambda_0 is not None:
        return {"v": c * (delta_lambda / lambda_0)}
    elif v is not None and lambda_0 is not None:
        return {"delta_lambda": (v / c) * lambda_0}
    elif v is not None and delta_lambda is not None:
        return {"lambda_0": delta_lambda / (v / c)}
    else:
        raise ValueError("Need two of the three values: delta_lambda, lambda_0, v")
