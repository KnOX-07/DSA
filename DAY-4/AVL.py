class node:
    def __init__(self,v):
        self.data=v
        self.left=None
        self.right=None
class AVLTree:
    def __init__(self):
        self.root=None
    def inorder(self,n):
        if n!=None:
            self.inorder(n.left)
            print(n.data)
            #print(self.balanceFactor(n))
            self.inorder(n.right)
    def preorder(self,n):
        if n!=None:
            print(n.data)
            self.preorder(n.left)
            self.preorder(n.right)

    def insert_node(self,v):
        n=node(v)
        if self.root==None:
            self.root=n
            return
        temp=self.root
        while temp!=None:
            par=temp
            if n.data<=temp.data:
                temp=temp.left
            else:
                temp=temp.right
        if n.data<=par.data:
            par.left=n
        else:
            par.right=n
        if self.balanceFactor(n) not in [0,-1,1]:
            print("Tree is unbalanced")
    def delete_node_no_child(self,par,temp):
        if temp.data<=par.data:
            par.left=None
        else:
            par.right=None
        del temp
    def delete_node_with_left_child(self,par,temp):
        if temp.data<=par.data:
            par.left=temp.left
        else:
return max(self.heigth(rt.left), self.height(rt.left))-1
            par.right=temp.left
        del temp
    def delete_node_with_right_child(self,par,temp):
        if temp.data<=par.data:
            par.left=temp.right
        else:
            par.right=temp.right
        del temp
    def delete(self,item):
        temp=self.root
        par=None
        while temp!=None and temp.data!=item:
            par=temp
            if item<=temp.data:
                temp=temp.left
            else:
                temp=temp.right
        if temp==None:
            print("Item not found in the tree")
            return
        else:
            if temp.left==None and temp.right==None:
                self.delete_node_no_child(par,temp)
            elif temp.left!=None and temp.right==None:
                self.delete_node_with_left_child(par,temp)
            elif temp.left==None and temp.right!=None:
                self.delete_node_with_right_child(par,temp)
            else:
                succ_par=temp
                succ=temp.right
                while succ.left!=None:
                    succ_par=succ
                    succ=succ.left
                print('successor of deleted item:',succ.data)
                print('Parent of successor of deleted item:',succ_par.data)
                succ_info=succ.data
                if succ.right!=None:
                    self.delete_node_with_right_child(succ_par,succ)
                else:
                    self.delete_node_no_child(succ_par,succ)
                temp.data=succ_info
    def height(self, rt) :
        if rt == None :
            return 0
        else :
            return max(self.height(rt.left), self.height(rt.left))+1

    def balanceFactor(self, rt) :
            return self.height(rt.left)-self.height(rt.right)

tr=AVLTree()
tr.insert(23)
tr.inorder(tr.root)
print("========")
tr.insert(73)
tr.inorder(tr.root)
print("========")
tr.insert(13)
tr.inorder(tr.root)
print("========")
tr.insert(53)
tr.inorder(tr.root)
print("========")
tr.insert(10)
tr.inorder(tr.root)
print("========")
tr.insert(24)
tr.insert(60)
tr.insert(65)
tr.insert(80)
tr.insert(85)
tr.insert(75)
tr.inorder(tr.root)
print("========")
print("Inorder traversal")
tr.inorder(tr.root)
#print("Preorder traversal")
#tr.preorder(tr.root)
tr.delete(73)
print("Inorder traversal")
tr.inorder(tr.root)
#print("Preorder traversal")
#tr.preorder(tr.root)
