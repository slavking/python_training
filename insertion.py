count = 0

def exchange(K, i ,j):
    print(str(K) + 'izmena ')
    global count
    count = count + 1
    temp = K[j]
    K[j] = K[i]
    K[i] = temp
    print(str(K)+' '+str(count))

def insertion_sort(L):
    a=L.copy()
    for i in range(len(L)):
        for j in range(i,0,-1) :
            if a[j]<a[j-1]:
                exchange(a, j, j-1)
            else: break
    
    return a

def stampaj_elem(K, i):
    string = '['
    for k in range(len(K)):
        if k != i:
            string += '-  '
        if k == i:
            string += str(K[i])
    string += ']'
    return string


def shellsort(L):
    gaps= [7,4,1]
    global count
    count = 0
    a=L.copy()
    for gap in gaps:
        for i in range(gap,len(L),1):
            temp = a[i]
            print(i)
            #sprint(stampaj_elem(a, i))
            j = i
            while (j >= gap and a[j - gap] > temp):
                
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
            count += 1
            print (str(a) + ' '+str(count))
    return a

def mergesort(A):
    # izgleda mora in-place
    print('Razdvajanje', A)
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        #sve ovo je u if klauzuli
        '''
        ako je najlevlji levi element manji od najlevljeg desnog
        onda u finalni merge ubaciti na poziciju K levi element
        i inkrementirati index levog
        u suprotnom, ubaciti najlevljeg desnog i inkrementirati
        index desnog
        '''
        
        print(str(A)+' leva polovina '+str(lefthalf)+' \
              desna polovina '+str(righthalf))
        while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    A[k] = lefthalf[i]
                    i += 1
                else:
                    A[k] = righthalf[j]
                    j += 1
                k += 1

        while i < len(lefthalf) :
                A[k] = lefthalf[i]
                i += 1
                k += 1

        while j < len(righthalf):
                A[k] = righthalf[j]
                j += 1
                k += 1

    print('Merging ', A)
    return A

L = [3,5,7,2,1,4,8,19,10,22,65,21,33]
print('insertion sort')
print(insertion_sort(L))
print('shell sort')
print(shellsort(L))

print(mergesort(L))

