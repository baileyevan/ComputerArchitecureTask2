from kmapFunctions import printKmap
from kmapFunctions import buildKmap
from groupingFunctions import findGroups
from groupingFunctions import groupToTerm
from validationFunctions import validateSimplifiedExpression


def printTruthTable(n, outputs):
    #print the truth table for n variables
    
    # generate variable names (A, B, C...)
    variables = [chr(65+i) for i in range(n)]
    
    #total number of rows in truth table
    rows = 2 ** n
    
    #print the header section
    header = " | ".join(variables) + " | Y"
    print("\nTruth Table")
    print(header)
    print("-" * len(header))
    
    #print each row of the truth table
    for i in range(rows):
        #convert index to binary input
        binary = format(i, f'0{n}b')
        row = " | ".join(binary) + " | " + outputs[i]
        print(row)

def generateExpression(n, outputs, form):
    #generate canonical boolean expression (SOP or POS)
    
    rows = 2 ** n
    variables = [chr(65+i) for i in range(n)]

    #stores expression terms
    expression = []
    
    #stores turth table data
    tableData = []

    for i in range(rows):

        #current input combination
        binary = format(i, f'0{n}b')
        
        #corresponding output value
        value = outputs[i]

        #store the row for structured output
        tableData.append({
            "inputs": binary,
            "output": value
        })

        #Sum Of Products (looking for 1's)
        if form == "SOP" and value == "1":

            term = ""

            for j in range(n):
                if binary[j] == "1":
                    
                    #variable is true
                    term += variables[j]
                else:
                    #variable is complemented
                    term += variables[j] + "'"

            expression.append(term)

        # Product Of Sums (looking for 0's)
        elif form == "POS" and value == "0":

            termParts = []

            for j in range(n):
                if binary[j] == "1":
                    termParts.append(variables[j] + "'")
                else:
                    termParts.append(variables[j])

            #combine literals with OR (+) inside parenthesis
            expression.append("(" + " + ".join(termParts) + ")")
    
    #combine all terms into a single expression string
    if form == "SOP":
        expressionString = " + ".join(expression)
    else:
        expressionString = "".join(expression)

    return expressionString, tableData

def main():
    #get number of variables from user
    n = int(input("Enter the number of variable (n >= 2): "))
    #validation of variable amount
    while (n < 2):
        n = int(input("The number of variables must be (n >= 2): "))
        
    #get expression form from user (SOP or POS)
    form = input("Enter form (SOP or POS): ").upper()
    while form not in ("SOP", "POS"):
        form = input("Enter form (SOP or POS): ").upper()

    #read truth table output from file
    filename = "truthTable.txt"
    with open(filename, "r") as file:
        outputs = file.read().replace(" ", "").replace("\n", "")

    #expected number of outputs in file given users number of variables
    expectedVariables = 2 ** n

    #validate correct number of outputs
    if len(outputs) != expectedVariables:
        print(f"Error: Expected {expectedVariables} outputs but got {len(outputs)}")
        return
    
    #validate only 0's and 1's are in the output file
    if any(bit not in "01" for bit in outputs):
        print("Error: File must only contain 0's or 1's")
        return
    
    #display the truth table
    printTruthTable(n, outputs)
    
    #generate canonical boolean expression
    expression, table = generateExpression(n, outputs, form)

    #store results in dictionary (not being used currently in output)
    result = {
        "variables": n,
        "form": form,
        "expression": expression,
        "truthTable": table
    }

    print("\nBoolean Expression: ")
    print(expression)

    #optional json output
    """
   
    print("\nJSON Output: ")
    print(json.dumps(result, indent=2))
    
    """
    
    #build and display the kmap
    kmap, rows, cols = buildKmap(n, outputs)
    printKmap(kmap, rows, cols)
    
    #find all the valid kmap groups given form
    groups = findGroups(kmap, form)
    
    #tracks cells already covered by groups
    covered = set()
    
    #stores simplified expression terms
    terms = []
    
    #sort groups by size, largest first for optimal grouping
    groups.sort(key=len, reverse=True)
    
    #select groups that cover new cells
    for g in groups:
        
        #identify cells not yet covered
        newCells = [cell for cell in g if cell not in covered]
        
        #skip groups that dont contribute new coverage
        if not newCells:
            continue
            
        #convert group to boolean term
        term = groupToTerm(g, rows, cols, n, form=form)
        
        if term:
            terms.append(term)
            
            #mark cells as covered
            covered.update(g)
    
        
    #construct simplified expressions
    if form == "SOP":
        simplified = " + ".join(terms)
    else:
        simplified = "".join(terms)
    
    print("\nSimplified Equation: ")
    print(simplified)
    print("\n")
    
    #validate simplified expression against truth table
    if validateSimplifiedExpression(n, simplified, outputs, form):
        print("\nValidation: !!!PASS!!!")
    else:
        print("\nValidation: FAILED...")



if __name__ == "__main__":
    main()