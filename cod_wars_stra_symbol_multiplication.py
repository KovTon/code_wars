def calculator(txt):
    ll = txt.split()
    n1 = ll[0].count(".")
    n2 = ll[2].count(".") 
    return {"+": n1+n2, "-": n1-n2, "*": n1*n2, "//": n1//n2}[ll[1]] * "."

