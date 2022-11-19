def showVertexList(list, sulfix = ""):
    if not(list):
        return sulfix + "(empty)"

    x = sulfix + ""

    for v in list:
        x = x + v.alias + " "
    
    return x