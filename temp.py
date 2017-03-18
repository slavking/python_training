class Node1:
    def __init__(self,x):
        self.x=x

class Node2(Node1):
    def __init__(self):
        while self is not None:
            yield self.x

from string import ascii_lowercase

def returner(x):
    return True if x in ascii_lowercase else False
