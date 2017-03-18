def apply(L,x):
    result=[]
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def sqr(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

