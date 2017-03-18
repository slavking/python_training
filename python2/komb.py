class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

               
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    def addWeight(self,edge):
        Digraph.addEdge(self,edge)
        rev=WeightedEdge(edge.getDestination(),edge.getSource(),edge.getWeight())
        Digraph.addEdge(self,rev)
    def __str__(self):
        result=''
        for src in self.edges:
            for dest in self.edges[src]:
                print(self.edges[src])
        return result[:-1]

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        #IN PROGRESS
        super(WeightedEdge,self).__init__(src,dest)
        self.weight=weight
        
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return self.src.getName() + '->' + self.dest.getName()+' ('+str(self.weight)+')'

    
##def buildCityGraph(Graphtype):
##    g = Graphtype()
##    for name in ('Boston', 'Providence', 'New York', 'Chicago',
##                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
##            g.addNode(Node(name))
##        
##    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
##    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
##    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
##    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
##    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
##    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
##    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
##    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
##    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
##    return g
##    
##print(buildCityGraph(Graph))


'''
    Consider our representation of permutations of students in a line from Exercise 1.
    (The teacher only swaps the positions of two students that are next to each other in line.)
    Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C).
    Using the Graph class created in the lecture, we can create a graph with the design chosen
    in Exercise 1: vertices represent permutations of the students in line;
    edges connect two permutations if one can be made into the other by swapping two adjacent students.

    We construct our graph by first adding the following nodes:
    '''

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

##g.addEdge(Edge(nodes[0], nodes[1]))
##g.addEdge(Edge(nodes[0], nodes[2]))
##g.addEdge(Edge(nodes[1], nodes[4]))
##g.addEdge(Edge(nodes[2], nodes[3]))
##g.addEdge(Edge(nodes[3], nodes[5]))
##g.addEdge(Edge(nodes[4], nodes[5]))

g.addWeight(WeightedEdge(nodes[0],nodes[1],3))
g.addWeight(WeightedEdge(nodes[0],nodes[2],4))

print(g)

##for x in nodes:
##    ynodes=nodes
##    ynodes.remove(x)
##    for y in ynodes:
##        if not x.getName() == y.getName():
##            if x.getName()[0] == y.getName()[0]:
##                #print(x.getName()[0],y.getName()[0])
##                g.addEdge(Edge(x,y))
##            elif x.getName()[1]==y.getName()[1]:
##                g.addEdge(Edge(x,y))

#digao ruke 
##            




    
    



'''Write your code in terms of the nodes list from the code above.
For each node, think about what permutation is allowed.
A permutation of a set is a rearrangement of the elements in that set.
In this problem, you are only adding edges between nodes whose permutations
are between elements in the set beside each other .
For example, an acceptable permutation (edge)
is between "ABC" and "ACB" but not between "ABC" and "CAB".
'''
