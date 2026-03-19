
def checkGroup(kmap, row, col, height, width, target):
    #get dimensions of the kmap
    rows = len(kmap)
    cols = len(kmap[0])
    
    #will be used to store coordinates of valid group cells
    cells = []
    
    #iterate over the group size (height x width)
    for dr in range(height):
        for dc in range(width):
            
            #wrap around using mod to check edges of kmap
            rr = (row + dr) % rows
            cc = (col + dc) % cols
            
            #if any cell does not match the target (1 for SOP and 0 for POS)
            #then the group is invalid
            if kmap[rr][cc] != target:
                return None
            
            #otherwise its valid and we add this cell to the group
            cells.append((rr,cc))
    
    #return the list of valid group cell positions
    return cells

def findGroups(kmap, form):
    #determine what value we are grouping
    #SOP = 1, POS = 0
    target = "1" if form == "SOP" else "0"
    
    rows = len(kmap)
    cols = len(kmap[0])
    
    #list to store all valid groups found
    groups = []
    
    #all possible group sizes (power of 2)
    sizes = [(1,1),(1,2),(2,1),(2,2),(1,4),(4,1),(2,4),(4,2),(4,4)]
    
    #try every possible group size
    for height,width in sizes:
        #skip sizes greater than size of kmap
        if height > rows or width > cols:
            continue
        
        #try every starting position in kmap
        for row in range(rows):
            for col in range(cols):
                
                #check if valid group exists at this position and size
                group = checkGroup(kmap, row, col, height, width, target)
                
                #if valid add it to the list
                if group:
                    groups.append(group)
    
    return groups

def groupToTerm(group, rowLabels, colLabels, n, form="SOP"):
    #generate variables names: A,B,C...
    variables = [chr(65+i) for i in range(n)]
    
    #convert group cell positions into binary strings
    binaries = []
    for row, col in group:
        binaries.append(rowLabels[row] + colLabels[col])
    
    #Sum Of Products Implementation
    if form == "SOP":
        term = ""
        
        #check each varibale position
        for i in range(n):
            #get all the bits for this variable across the group
            #this tells us if the variables stay the same accross the group
            bits = {b[i] for b in binaries}
            
            #if all the bits are the same this variable is part of the term
            #keep only variables that dont change
            if len(bits) == 1:
                
                #build the term
                if "1" in bits:
                    # variable stays normal
                    term += variables[i]
                else:
                    #variable is complemented
                    term += variables[i] + "'"
        return term
    
    #Product Of Sums Implementation
    elif form == "POS":
        literals = []
        for i in range(n):
            bits = {b[i] for b in binaries}
            
            if len(bits) == 1:
                #POS uses opposite logic of SOP
                if "0" in bits:
                    #normal variable
                    literals.append(variables[i])
                else:
                    #compliment
                    literals.append(variables[i] + "'")
                   
        #sort literals alphabetically for consistent output (A then B then C) 
        literals.sort(key=lambda x: variables.index(x[0]))
        
        #join literals with OR (+) inside parenthasis
        term = "(" + " + ".join(literals) + ")"
        
        return term
