from kmapFunctions import printKmap
from kmapFunctions import buildKmap
from groupingFunctions import findGroups
from groupingFunctions import groupToTerm


def printTruthTable(n, outputs):
    variables = [chr(65+i) for i in range(n)]
    rows = 2 ** n
    
    header = " | ".join(variables) + " | Y"
    print("\nTruth Table")
    print(header)
    print("-" * len(header))
    for i in range(rows):
        binary = format(i, f'0{n}b')
        row = " | ".join(binary) + " | " + outputs[i]
        print(row)

def generateExpression(n, outputs, form):
    rows = 2 ** n
    variables = [chr(65+i) for i in range(n)]

    expression = []
    tableData = []

    for i in range(rows):

        binary = format(i, f'0{n}b')
        value = outputs[i]

        tableData.append({
            "inputs": binary,
            "output": value
        })

        # SOP (minterms)
        if form == "SOP" and value == "1":

            term = ""

            for j in range(n):
                if binary[j] == "1":
                    term += variables[j]
                else:
                    term += variables[j] + "'"

            expression.append(term)

        # POS (maxterms)
        elif form == "POS" and value == "0":

            termParts = []

            for j in range(n):
                if binary[j] == "1":
                    termParts.append(variables[j] + "'")
                else:
                    termParts.append(variables[j])

            expression.append("(" + " + ".join(termParts) + ")")
            
    if form == "SOP":
        expressionString = " + ".join(expression)
    else:
        expressionString = "".join(expression)

    return expressionString, tableData

def main():
    n = int(input("Enter the number of variable (n >= 2): "))
    while (n < 2):
        n = int(input("The number of variables must be (n >= 2): "))
           
    form = input("Enter form (SOP or POS): ").upper()
    while form not in ("SOP", "POS"):
        form = input("Enter form (SOP or POS): ").upper()

    filename = "truthTable.txt"
    with open(filename, "r") as file:
        outputs = file.read().replace(" ", "").replace("\n", "")

    expectedVariables = 2 ** n

    if len(outputs) != expectedVariables:
        print(f"Error: Expected {expectedVariables} outputs but got {len(outputs)}")
        return
    
    if any(bit not in "01" for bit in outputs):
        print("Error: File must only contain 0's or 1's")
        return
    
    printTruthTable(n, outputs)
    expression, table = generateExpression(n, outputs, form)

    result = {
        "variables": n,
        "form": form,
        "expression": expression,
        "truthTable": table
    }

    print("\nBoolean Expression: ")
    print(expression)

    """
   
    print("\nJSON Output: ")
    print(json.dumps(result, indent=2))
    
    """
    
    kmap, rows, cols = buildKmap(n, outputs)
    printKmap(kmap, rows, cols)
    
    groups = findGroups(kmap, form)
    
    covered = set()
    terms = []
    
    groups.sort(key=len, reverse=True)
    
    for g in groups:
        # check if group covers any cells
        newCells = [cell for cell in g if cell not in covered]
        
        if not newCells:
            continue
            
        term = groupToTerm(g, rows, cols, n, form=form)
        
        if term:
            terms.append(term)
            covered.update(g)
    
            
    if form == "SOP":
        simplified = " + ".join(terms)
    else:
        simplified = "".join(terms)
    
    print("\nSimplified Equation: ")
    print(simplified)



if __name__ == "__main__":
    main()