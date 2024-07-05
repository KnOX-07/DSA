class Node:
    def __init__(self, v):
        self.info = v
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.start = None
           
    def InsertAtBeg(self, v):
        n = Node(v)
        n.next = self.start
        self.start = n 
        return self.start
     
    def DeleteFromBeg(self):
        n = self.start
        self.start = self.start.next
        del n
        return self.start 
      
    def InsertAtLast(self, v):
        n = Node(v)
        if self.start == None:
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
            
    def DeleteLastNode(self):
        temp = self.start
        while temp.next != None:
            prev = temp
            temp = temp.next
        del temp
        prev.next = None
        
    def InsertSpecificItem(self, item):
        p = int(input("Enter new node: "))
        new = Node(p)
        temp = self.start
        while temp!= None and temp.info!= item:
            temp = temp.next
        if temp == None:
            print("Error: Specified node not found in the linked list.")
            return
        new.next = temp.next
        temp.next = new
        return self.start
    
    def DeleteSpecificItem(self, item):
        temp = self.start
        while temp != None and temp.info != item:
            prev = temp
            temp = temp.next
        if temp != None:
            prev.next = temp.next
            del temp
        else:
            print("Item does not exist!!")
            
    def InsertAtPos(self, pos):
        q = int(input("Enter a new node: "))
        new = Node(q)
        temp = self.start 
        for i in range(1, pos-1):
            temp = temp.next
        new.next = temp.next 
        temp.next = new
        
    def DeleteAtPos(self, pos):
        temp = self.start 
        for i in range(1, pos):
            prev = temp
            temp = temp.next
        if temp != None:
            prev.next = temp.next    
            del temp   
            
    def Traverse(self):    
        n = self.start
        while n != None:
            print(n.info)
            n = n.next
            print("⇣")
        print("None")
            
sl = SingleLinkedList()
sl.InsertAtLast(12)
sl.InsertAtLast(24)
sl.InsertAtLast(55)
sl.InsertAtBeg(10)
sl.Traverse()
print("=======")
sl.DeleteFromBeg()
sl.Traverse()
print("=======")
sl.DeleteLastNode()
sl.Traverse()
print("=======")
item = int(input("Enter specific node before inserting a new node: "))
sl.InsertSpecificItem(item)
sl.Traverse()
print("=======")
item = int(input("Enter the node which you want to delete: "))
sl.DeleteSpecificItem(item)
sl.Traverse()
print("=======")
pos = int(input("Enter position where you want to insert a new node: "))
sl.InsertAtPos(pos)
sl.Traverse()
print("=======")
pos = int(input("Enter position where you want to delete a node: "))
sl.DeleteAtPos(pos)
sl.Traverse()