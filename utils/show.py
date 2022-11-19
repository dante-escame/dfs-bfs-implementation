def showVertexList(list, sulfix = ""):
    x = sulfix + ""
    for v in list:
        x = x + v.alias + " "
    return x