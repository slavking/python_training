def deep_reverse(L):
    
#For example, if L = [[1, 2], [3, 4], [5, 6, 7]]
#then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

    for x in L:
        x.reverse()
    L.reverse()

#L=[[1,2],[3,4],[5,6,7]]
#L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
#print(L)
#deep_reverse(L)
#print(L)
    
            
