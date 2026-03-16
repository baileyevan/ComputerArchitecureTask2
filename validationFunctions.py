def validateSimplifiedExpression(n, simplifiedExpr, outputs, form):

    variables = [chr(65+i) for i in range(n)]
    rows = 2 ** n
    success = True

    for i in range(rows):

        bits = format(i, f'0{n}b')
        values = {var: int(bit) for var, bit in zip(variables, bits)}

        if form == "SOP":
            result = evaluateSOP(simplifiedExpr, values)
        else:
            result = evaluatePOS(simplifiedExpr, values)
            
        print(f"{bits} -> expected {outputs[i]}, got {result}")

        if result != int(outputs[i]):
            print(f"Mismatch for input {bits}: expected {outputs[i]}, got {result}")
            success = False

    return success

def evaluateSOP(expr, values):

    terms = expr.split("+")

    for term in terms:

        term = term.strip()
        term_value = 1

        i = 0
        while i < len(term):

            var = term[i]

            if i+1 < len(term) and term[i+1] == "'":
                term_value &= (not values[var])
                i += 1
            else:
                term_value &= values[var]

            i += 1

        if term_value:
            return 1

    return 0

def evaluatePOS(expr, values):

    groups = expr.replace("(", "").split(")")

    for group in groups:

        group = group.strip()
        if not group:
            continue

        literals = group.split("+")
        group_value = 0

        for literal in literals:

            literal = literal.strip()

            if literal.endswith("'"):
                var = literal[0]
                group_value |= (not values[var])
            else:
                group_value |= values[literal]

        if not group_value:
            return 0

    return 1