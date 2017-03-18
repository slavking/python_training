import random

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]
          

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]


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
          

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            print('i '+str(i))
            print('j '+str(j))
            print(str(i>>j))
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
    
#def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    n=len(items)
    for i in range(3**n):
        combo1=[]
        combo2=[]
        for j in range(n):
            if (i//3**j) % 3 == 2:
                combo1.append(items[j])
            elif (i//3**j) % 3 == 1:
                combo2.append(items[j])
        yield (combo1,combo2)
    
#b=buildRandomItems(3)
#p=powerSet(b)

#while True:
#    L=next(p)
#    for i in L:
#        print(i)
#    print('\n')

