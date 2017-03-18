def f(a,b):
    return a+b

def dict_interdiff(d1,d2):
    #vraca tupl, gde je prvi clan presek d1 i d2 a drugi razlika
    #tuple(inter(d1,d2),diff(d1,d2))
    inter={}
    diff={}
    for x in d1:
        if x in d2:
            inter[x]=f(d1[x],d2[x])
    for x in d1:
        if not x in d2:
           diff[x]=d1[x]
    for x in d2:
        if not x in d1:
            diff[x]=d2[x]
    return (inter,diff)



'''
    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns
    ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    If f(a, b) returns a > b
    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}
    then dict_interdiff(d1, d2) returns
    ({1: False, 2: False, 3: False}, {})
'''
            
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d1 = {1:30, 2:20, 3:30, 5:80}
