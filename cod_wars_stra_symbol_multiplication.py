def calculator(txt):
    ll = txt.split()
    n1 = ll[0].count(".")
    n2 = ll[2].count(".")
    return {"+": n1+n2, "-": n1-n2, "*": n1*n2, "//": n1//n2}[ll[1]] * "."


# Это идеальное и красивое решение(Паша)


def calculator_ideal(txt):
    a, op, b = txt.split()
    a, b = len(a), len(b)
    return '.' * eval(f'{a} {op} {b}')
