def oddTuples(aTup):

    L=[]
    for i in range(0,len(aTup),2):
        L.append(aTup[i])

    return tuple(L)
    
