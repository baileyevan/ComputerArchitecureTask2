def printKmap(kmap, rowLabels, colLabels):
    print("\nKarnaugh Map\n")
    
    #print Column Headers
    print("     ", end = "")
    for col in colLabels:
        #right align for spacing
        print(f"{col:>4}", end="")
    print()
    
    #seperate header from actual table
    print("    +" + "----"*len(colLabels))
    
    #print each row of kmap
    for i, row in enumerate(kmap):
        #print row label
        print(f"{rowLabels[i]:>3} |", end="")
        
        #print each cell value in the row
        for val in row:
            print(f"{val:>4}", end="")
        print()
    print()
    
def wrap(i, size):
    #uitlity function for wrap around indexing
    #ensures indices stay within bounds
    return i % size


def buildKmap(n, outputs):
    #build the kmap structure based on number of variables
    
    #define row and col labels
    #ensure only 1 bit changes
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
    
    #fill the kmap using the truth table outputs
    for r in rowLabels:
        row = []
        for c in colLabels:
            
            #combine row and col labels to form binary input
            binary = r + c
            
            #convert binary string to decimal index
            index = int(binary,2)
            
            #use index to fetch corresponding output value
            row.append(outputs[index])
        
        #add completed row to kmap
        kmap.append(row)
    
    return kmap, rowLabels, colLabels
