def printKmap(kmap, rowLabels, colLabels):
    print("\nKarnaugh Map\n")
    
    # Print Column Headers
    print("     ", end = "")
    for col in colLabels:
        print(f"{col:>4}", end="")
    print()
    
    print("    +" + "----"*len(colLabels))
    
    # Print Rows
    for i, row in enumerate(kmap):
        print(f"{rowLabels[i]:>3} |", end="")
        for val in row:
            print(f"{val:>4}", end="")
        print()
    print()
    
def wrap(i, size):
    return i % size


def buildKmap(n, outputs):
    if n == 2:
        rowLabels = ["0","1"]
        colLabels = ["0","1"]
    elif n == 3:
        rowLabels = ["0","1"]
        colLabels = ["00","01","11","10"]
    elif n == 4:
        rowLabels = ["00","01","11","10"]
        colLabels = ["00","01","11","10"]
        
    kmap = []
    
    for r in rowLabels:
        row = []
        for c in colLabels:
            binary = r + c
            index = int(binary,2)
            row.append(outputs[index])
        
        kmap.append(row)
    
    return kmap, rowLabels, colLabels
