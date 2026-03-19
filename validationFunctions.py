def validateSimplifiedExpression(n, simplifiedExpr, outputs, form):
    #validate the simplified boolean expression by comparing its output
    #against the original truth table for all input combinations

    #generate variable names
    variables = [chr(65+i) for i in range(n)]
    #total number of input combinations
    rows = 2 ** n
    #tracks state of validation
    success = True

    for i in range(rows):

        #current input combinations as a binary string
        bits = format(i, f'0{n}b')
        
        #map variables to their corresponding values (A=0, B=1,...)
        values = {var: int(bit) for var, bit in zip(variables, bits)}

        #evaluate the simplified expression based on selected form
        if form == "SOP":
            result = evaluateSOP(simplifiedExpr, values)
        else:
            result = evaluatePOS(simplifiedExpr, values)
        
        #print comparison for debugging/verificatioin
        print(f"{bits} -> expected {outputs[i]}, got {result}")

        #check if result matches expected truth table output
        if result != int(outputs[i]):
            print(f"Mismatch for input {bits}: expected {outputs[i]}, got {result}")
            success = False

    return success

def evaluateSOP(expr, values):
    #evaluate a Sum Of Products expression

    #split expression into individual product terms (OR sperated)
    terms = expr.split("+")

    for term in terms:

        term = term.strip()
        #start with True
        term_value = 1

        i = 0
        while i < len(term):

            var = term[i]

            #check if variable is complemented
            if i+1 < len(term) and term[i+1] == "'":
                #apply NOT
                term_value &= (not values[var])
                #skiip the apostrophe
                i += 1
            else:
                #use variable value directly
                term_value &= values[var]

            i += 1

        #if any product term evaluates to True, entire SOP is true
        if term_value:
            return 1
        
    #if no terms evaluate to True, result is False
    return 0

def evaluatePOS(expr, values):
    #evaluate a Product Of Sums expression
    
    #remove opening parentheses and split into sum groups
    groups = expr.replace("(", "").split(")")

    for group in groups:

        group = group.strip()
        if not group:
            
            #skip empty groups
            continue

        #split group into literals (OR seperated)
        literals = group.split("+")
        
        #start with False
        group_value = 0

        for literal in literals:

            literal = literal.strip()

            #check if literal is complemented
            if literal.endswith("'"):
                var = literal[0]
                
                #apply NOT
                group_value |= (not values[var])
            else:
                #use variable value directly
                group_value |= values[literal]

        #if any group evaluates to False, entire POS is False
        if not group_value:
            return 0

    #if all groups evaluate True, result is True
    return 1