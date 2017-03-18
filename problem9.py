'''Write a function to flatten a list.
The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
'''
#http://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(aList):

    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == [] :
        return []
                          
    return flatten(aList[0]) + (flatten(aList[1:])\
    if len(aList) > 1 else []) if type(aList) is list else [aList]  


L=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
A=[[],[]]
B=[]

flatten(L)
