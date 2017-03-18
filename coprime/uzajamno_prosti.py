from collections import deque

def coprimes():
  tree = deque([[2, 1], [3, 1]])
  while True:
    m, n = tree.popleft()
    yield m, n
    tree.append([2 * m - n, m])
    tree.append([2 * m + n, m])
    tree.append([m + 2 * n, n])


generator = coprimes()
i = 1
while  i< 10000 :
  s=next(generator)
  if s <= (10,10):
    print(s)
  i=i+1
  
    

#for i in generator:
#    if i <= (8,8):
#        print(i)
#    if i > (1000,1000)
#      break

  





