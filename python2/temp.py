class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'


def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]
          
def yiel(L):
    
    n=len(L)
    for i in range(3**n):
        combo1=[]
        combo2=[]
        for j in range(n):
            print('i '+str(i))
            print('j '+str(j))
            print(i//3**j)
            if (i//3**j) % 3 == 2:
                combo1.append(L[j])
            elif (i//3**j) % 3 == 1:
                combo2.append(L[j])
        yield (combo1,combo2)

L=[1,2]

p=variations(L)
count=1
while True:
    for i in next(p):
        print(i)
        print(count)
    print('\n')
    count+=1
'''  n=len(items)
    for i in range(3**n):
        combo1=[]
        combo2=[]
        for j in range(n):
            if (i//3**j) % 3 == 2:
                combo1.append(items[j])
            elif (i//3**j) % 3 == 1:
                combo2.append(items[j])
        yield (combo1,combo2)
'''
    
