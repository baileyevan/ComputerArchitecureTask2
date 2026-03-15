def checkGroup(kmap, row, col, height, width, target):
    rows = len(kmap)
    cols = len(kmap[0])
    
    cells = []
    
    for dr in range(height):
        for dc in range(width):
            
            rr = (row + dr) % rows
            cc = (col + dc) % cols
            
            if kmap[rr][cc] != target:
                return None
            
            cells.append((rr,cc))
    
    return cells

def findGroups(kmap, form):
    target = "1" if form == "SOP" else "0"
    
    rows = len(kmap)
    cols = len(kmap[0])
    
    groups = []
    
    sizes = [(1,1),(1,2),(2,1),(2,2),(1,4),(4,1),(2,4),(4,2),(4,4)]
    
    for height,width in sizes:
        if height > rows or width > cols:
            continue
        
        for row in range(rows):
            for col in range(cols):
                
                group = checkGroup(kmap, row, col, height, width, target)
                
                if group:
                    groups.append(group)
    
    return groups

def groupToTerm(group, rowLabels, colLabels, n, form="SOP"):
    variables = [chr(65+i) for i in range(n)]
    
    binaries = []
    for row, col in group:
        binaries.append(rowLabels[row] + colLabels[col])
    
    if form == "SOP":
        term = ""
        for i in range(n):
            bits = {b[i] for b in binaries}
            if len(bits) == 1:
                if "1" in bits:
                    term += variables[i]
                else:
                    term += variables[i] + "'"
        return term
    
    elif form == "POS":
        literals = []
        for i in range(n):
            bits = {b[i] for b in binaries}
            if len(bits) == 1:
                if "0" in bits:
                    literals.append(variables[i])
                else:
                    literals.append(variables[i] + "'")
                    
        literals.sort(key=lambda x: variables.index(x[0]))
        term = "(" + " + ".join(literals) + ")"
        
        return term
