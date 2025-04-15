def solve(knowns):
    Rp = knowns.get("Rp") 
    Rs = knowns.get("Rs")
    d = knowns.get("d")    

    if Rp is not None and Rs is not None:
        return {"d": (Rp / Rs) ** 2}
    elif d is not None and Rs is not None:
        return {"Rp": Rs * (d ** 0.5)}
    elif d is not None and Rp is not None:
        return {"Rs": Rp / (d ** 0.5)}
    else:
        raise ValueError("Need two of the three values: Rp, Rs, d")
