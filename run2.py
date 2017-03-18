L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#L=[5,4,10]

def longest_run(L):

    if len(L)==2:
        return L[0]+L[1]

    if not L:
        return []
   

    pileinc=[[L[0]]]
    piledec=[[L[0]]]
    
    for i in range(1,len(L)):
        newnode=L[i]
        #print(newnode)
        #print(max(pileinc[-1]))
        if   max(pileinc[-1]) <= newnode:
            pileinc[-1].append(newnode)
        else:
            pileinc.append([newnode])


        if  min(piledec[-1]) >= newnode :
            piledec[-1].append(newnode)
        else :
            piledec.append([newnode])

        #c=input("enter")
        
        

    print(pileinc)
    print(piledec)

    maxintsublist=0
    indexinc=0
    maxdecsublist=0
    indexdec=0


    
    for i in range(len(pileinc)):
        if len(pileinc[i]) > maxintsublist:
            maxintsublist=len(pileinc[i])
            indexinc=i

    for i in range(len(piledec)):
        if len(piledec[i]) > maxdecsublist:
            maxdecsublist=len(piledec[i])
            indexdec=i
            
   # print(indexinc)
   # print(indexdec)
   # print (pileinc[indexinc])
   # print (piledec[indexdec])
    if maxintsublist > maxdecsublist:
        return pileinc[indexinc]
    elif maxintsublist < maxdecsublist:
        return piledec[indexdec]
    else:
        if indexinc < indexdec:
            return pileinc[indexinc]
        else:
            return piledec[indexdec]

longest_run(L)
