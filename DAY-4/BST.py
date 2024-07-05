class Node:
    def __init__(self,v):
        self.info = v
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def Create(self,v):
        n = Node(v)
        if self.root == None:
            self.root = n
        
        temp = self.root
        while temp != None:
            if n.info < temp.info:
                par = temp
                temp = temp.left
            else:
                par = temp
                temp = temp.right
                
        if n.info < par.info:
            par.left = n
        else:
            par.right = n

    def inorder(self,n):
        if Node != None:
            self.inorder(Node.left)
            print(Node.info)
            self.inorder(Node.right)

t = BST()
t.Create(100)
t.Create(50)
t.Create(130)
t.Create(160)
t.Create(90)
t.Create(20)
t.Create(110)
t.inorder()
