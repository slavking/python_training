#flatten a list
#da izravna listu

L=[[3,4,5],[4,[5,6,[6]]],[4],5]

def flatten(aList): 
    if aList == [] :
        return []

    print(aList)
                          
    return flatten(aList[0]) + (flatten(aList[1:])\
    if len(aList) > 1 else []) if type(aList) is list else [aList] 

X=flatten(L)
print(X)
