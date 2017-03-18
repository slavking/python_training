


def create_table(string):
    
    D={}
    for x in string:
        D[x]=0
    for x in string:
        D[x]+=1
    for x in D:
        D[x]=round(D[x]/len(string)*100)
    L = [ (x,D[x]) for x in D]
    L.sort(key = lambda x:(-x[1],x[0]))
    return L

lorem='loremipsumdolor'
print(len(lorem))
A= create_table('loremipsumdolor')
print(A)

    
