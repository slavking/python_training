def dotProduct(listA, listB):

    def productTuple(A):
        return A[0]*A[1]
    
    return sum(map(productTuple,zip(listA,listB)))
  


listA= [1,2,3]
listB=[4,5,6]
print(listA)
print(listB)

print(dotProduct(listA,listB))
