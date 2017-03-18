from collections import namedtuple
from sys import stdout

Node = namedtuple('Node', 'data, left, right')
tree = Node(15,
            Node(8,
                 Node(4,
                      None, Node(6, None, None)),
                 Node(13,
                      Node(12, None, None),
                      None)),
            Node(33,
                 Node(27,
                      Node(20, None,
                           Node(22, None, None)),
                      None),
                 Node(41, None, None)))

tree2= Node('A',
            Node('B', None,
                 Node('D', None, None)),
            Node('C',
                 Node('E', None, None),
                 None))

tree1b = Node('C',
            Node ('B', None,
                Node('D', None, None)),
            Node('C',
                 Node('E', None, None),
              Node ('C', None, None)))

tree2011=Node('K',
              Node('G',
                   Node('A',None,
                        Node('F',
                             Node('E',None,None), None)),
                   Node('H',None,None)),
              Node('B',
                     Node('I',None,None),
                     Node('C',
                          Node('D',None,None),
                          Node('J',None,None))))

tree2007=Node('A',
              Node('G',
                   None,
                   Node('K', None, None)),
              Node ('B',
                    Node('C',
                         Node('F',
                              None,
                              Node('H',None,None)),
                         Node('D',
                              Node('J',None,None),
                              None
                              )),                       
                    Node('E',
                         Node('I',None,None),
                         None
                         )))



def printwithspace(i): #celi brojevi, baguje sa slovima
    stdout.write("%i " % i)

def printwithspace_char(i): #radi i sa brojevima i sa slovima
    print(i,end = ' ')
 
def preorder(node, visitor = printwithspace_char):
    if node is not None:
        visitor(node.data)
        preorder(node.left, visitor)
        preorder(node.right, visitor)
 
def inorder(node, visitor = printwithspace_char):
    if node is not None:
        inorder(node.left, visitor)
        visitor(node.data)
        inorder(node.right, visitor)
 
def postorder(node, visitor = printwithspace_char):
    if node is not None:
        postorder(node.left, visitor)
        postorder(node.right, visitor)
        visitor(node.data)
 
def levelorder(node, more=None, visitor = printwithspace_char):
    if node is not None:
        if more is None:
            more = []
        more += [node.left, node.right]
        visitor(node.data)
    if more:    
        levelorder(more[0], more[1:], visitor)

class stack(list): #prosiruje klasu list i pravi od nje stek
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self

def mirrorEqual(node1,node2):
    l=node1
    r=node2
    #print(l)
    #print(r)
    if l == None or r  == None:
        return l == None and r==None
    return mirrorEqual(l.left, r.right) and mirrorEqual(l.right, r.left)



s=stack([])
v=stack([])
l=stack([])

rightness=0
leftness=0
depth=0

def preorderI(root):
    s.push(root)
    #level=0
    #l.push(level)
    while (not s.isEmpty()):
        next=s.pop();
        #level-=1
        while next != None:
            visit(next)
            #l.push(level)
            if (next.right != None):
                s.push(next.right)
                #level+=1
            next=next.left
            

    return print('\n')

def inorderI(root):
    pass



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def enq(self,item):
        self.items.insert(0,item)

    def deq(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def levelorderI(root):
    q=Queue()
    curr=root
    q.enq(curr)
    height=0
    height_list=[]
    while ( not q.isEmpty()):
        nodeCount=q.size()
        if nodeCount == 0 : return height
        height +=1
        while (nodeCount>0):
            curr=q.deq()
            nodeCount -= 1
            visit(curr)
            if (curr.left != None):
                q.enq(curr.left)
            if (curr.right != None):
                q.enq(curr.right)        
    return height
   
def visit(node):
    printwithspace_char(node.data)
    v.push(node.data)
    return v

def visit_level(depth,leftness,rightness,node):
    l.push(depth)
    l.push(leftness)
    l.push(rightness)
    l.push(node)
    return l

def printstack(stack):
    for x in stack:
        printwithspace_char(x)
    print('\n')
    
#da li je drvo simetricno - iterativni algoritam - nije reseno
#napraviti mirror drveta, iterativni algoritam - reseno

def mirror_treeI(root):
    if (root== None): #check if the root of the tree is empty
        return None #return None if true

    q=Queue() #create Queue instance
    q.enq(root) #enqueue the root
    
    while (not q.isEmpty()): #while the queue is not empty
        temp = q.deq() #deque the first item at the head of queue
        #print(temp)
        if (temp == None): #this is a bugfix
            break
        swap=Node(getattr(temp,'data'),getattr(temp,'right'),
                  getattr(temp,'left')) #create a copy of the node
        #with swapped left and right subtrees
##        temp2 = temp._replace(left=swap.right,right=swap.left)
        if (temp== root): #if the temporary value (temp) equals (root)
            root2=swap   # create the return value root2
        if (swap.left != None) :# if the left subtree is not empty
            q.enq(swap.left) #enqueue it 
        if (swap.right != None): #same for the right subtree
            q.enq(swap.right)

    return root2

def mirror_tree(root):
    #traverse left subtree
    #traverse right subtree
    #temp = tree.left
    #tree.left=tree.right
    #tree.right=temp
    if (root.left != None):
        mirror_tree(root.left)
    if (root.right !=None):
        mirror_tree(root.right)
    return Node(getattr(root,'data'), getattr(root,'right'),
                getattr(root,'left'))

def mirror_equalI(root, L):
    if (root == None):
        return True
    s = stack([])

    def empty():
        pass
    
    def visitor_helper(node, data):
            p=str(data)+' '
            for x in s:
                p+=str(x)
            L.append(p)
                     
    def left_visit():
            s.push(0)
        
    def right_visit():
            s.push(1)
        
    def inorder_helper(node, function):
        
        if node is not None:
            function()
            inorder_helper(node.left, left_visit)
            visitor_helper(node, node.data)
            inorder_helper(node.right, right_visit)
            if not s.isEmpty():
                s.pop()

    inorder_helper(root, empty)
    

 
stdout.write('  preorder: ')
preorder(tree)
stdout.write('\n   inorder: ')
inorder(tree)
stdout.write('\n postorder: ')
postorder(tree)
stdout.write('\nlevelorder: ')
levelorder(tree)
stdout.write('\n')
print('\n Preorder iterativni')
preorderI(tree)
#stdout.write('\n')
print('\n Preorder iterativni')
preorderI(tree2)
#stdout.write('\n')
print('Da li je drvo tree1a simetricno?')
inorder(tree2)
stdout.write('\n')
print(mirrorEqual(tree2.left,tree2.right))
      
#printstack(v)

#printstack(l)
print('levelorder traversal iterativni: ')
K=levelorderI(tree)
print('\n visina ='+str(K))
K=levelorderI(tree2)
print('\n visina ='+str(K))
#tree3=mirror_treeI(tree2)
print('mirror drveta 1a ')
tree3=mirror_tree(tree2)
inorder(tree3)
stdout.write('\n')
print('Da li je simetricno?')
print(mirrorEqual(tree3.left,tree3.right))
#levelorderI(tree3)
print('\n')

print('Preorder')
preorder(tree3)
print('\n')
print('Inorder')
inorder(tree3)
print('\n ')
print('Postorder')
postorder(tree3)
print('\n')
#print(tree3)

print(' Da li je drvo tree1b simetricno? ')
K=levelorderI(tree1b)
print(mirrorEqual(tree1b.left,tree1b.right))

print(' Da li je drvo tree simetricno? ')
K = levelorderI(tree)
print(mirrorEqual(tree.left,tree.right))

A=[]
mirror_equalI(tree, A)
print(A)
A=[list(x.split(' ')[1]) for x in A]
print(A)
K=[]
mirror_equalI(tree2, K)
print(K)
K=[(x.split(' ')[1]) for x in K]
print(K)

L=[]
mirror_equalI(tree1b,L)
print(L)
L=[list(x.split(' ')[1]) for x in L]
              

def bitvector(L):

    #print(len(L))
    #print(len(L)%2)
    if len(L)% 2 == 0 :
        return False
    i=0
    j=len(L)-1
    flag=True
    while not i == j :
            x = L[i]
            y = L[j]
##            print('x ' +str(x))
##            print('y '+str(y))
            k = 0
            l = len(y)-1
            while k < len(x) and l > 0:
                a = x[k]
                b = y[k]
##                print('a '+str(a))
##                print('b '+str(b))
                if not ((x[k] == '0' and y[k] == '1') or (
                        x[k] == '1' and y[k] == '0')) :
                        flag = False
                k+=1
                l-=1
            i+=1
            j-=1

    return flag
    
        
    

print(bitvector(K))
print(bitvector(A))
print(bitvector(L))

def find_deepest_char(root, c):
    if (root == None):
        print('Prazno!')
        return False
    q=Queue() #create Queue instance
    q.enq(root) #enqueue the root
    print(levelorderI(root))          
    curr=root
    height=0
    height_list=[]
    while ( not q.isEmpty()):
        nodeCount=q.size()
        if nodeCount == 0 : return height_list.append((False,height))
        height +=1
        while (nodeCount>0):
            curr=q.deq()
            nodeCount -= 1
            if c == curr.data:
                height_list.append((curr.data,height))
            if (curr.left != None):
                q.enq(curr.left)
            if (curr.right != None):
                q.enq(curr.right)        
    return height_list[-1] if \
        len(height_list)>0 else False

L =find_deepest_char(tree1b,'C')
print(L)

inorder(tree2011)
print('\n inorder drvo kolokvijum 2011')
preorder(tree2011)
print('\n preorder drvo k2011')

inorder(tree2007)
print('\n inorder drvo k2007')
postorder(tree2007)
print('\n postorder drvo k2007')

postorder(tree2)
print('\n postorder')
postorder(tree1b)
print('\n postorder')
    




                      
                           
                    
