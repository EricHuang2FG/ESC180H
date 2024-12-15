def ev(expr):
    operations = []
    for element in expr:
        if element in ["+", "-", "*"]:
            operations.append(element)
    expr = expr.replace("+", "-").replace("*", "-").split("-")
    complete_expr = []
    for i in range(len(expr) - 1):
        pass

ev("14-3*2")
