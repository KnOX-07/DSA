class node:
    def __init__(self, value):
        self.info = value
        self.next = None
        
'''start = node(24)
start.next = node(12)
print(start.info)   #24
print(start.next)   #addr of next node       
print(start.next.info)  #12
print(start.next.next)  #None'''

def InsertAtLast(start):
    last = start
    for i in range(n1):
        v = int(input("Enter node: "))
        a = node(v)
        last.next = a
        last = a
                           
def InsertAtBeginning(start):
    x = int(input("Enter node you want to insert at beginning: "))
    new = node(x)
    new.next = start
    start = new
    return start  

def DeleteFromBeginning(start):
    n = start
    start = start.next 
    del n
    return start

def DeleteLastNode(start):
    temp = start
    while temp.next != None:
        prev = temp
        temp = temp.next
    del temp
    prev.next = None 
      
def InsertSpecificItem(start, item):
    p = int(input("Enter new node: "))
    new = node(p)
    temp = start
    while temp!= None and temp.info!= item:
        temp = temp.next
    if temp == None:
        print("Error: Specified node not found in the linked list.")
        return
    new.next = temp.next
    temp.next = new
    return start

def DeleteSpecificItem(start, item):
    temp = start
    while temp != None and temp.info != item:
        prev = temp
        temp = temp.next
    if temp != None:
        prev.next = temp.next
        del temp
    else:
        print("Item does not exist!!")
        
def InsertAtPos(start, pos):
    q = int(input("Enter a new node: "))
    new = node(q)
    temp = start 
    for i in range(1, pos-1):
        temp = temp.next
    new.next = temp.next 
    temp.next = new
    
def DeleteAtPos(start, pos):
    temp = start 
    for i in range(1, pos):
        prev = temp
        temp = temp.next
    if temp != None:
        prev.next = temp.next    
        del temp

def Traverse(start):
    n = start
    while n!= None:
        print(n.info)
        n = n.next
        print("⇣")
    print("None")
           
n1 = int(input("How many nodes you want to create: "))
n2 = int(input("Enter first node: "))
start = node(n2)
InsertAtLast(start)
print("After inserting nodes at last:-")
Traverse(start)
start = InsertAtBeginning(start)
print("After inserting new node at beginning:-")
Traverse(start)
start = DeleteFromBeginning(start)
print("After deleting from beginning your linked list is:-")
Traverse(start)
DeleteLastNode(start)
print("After deleting last node your linked list is:-")
Traverse(start)
item = int(input("Enter specific node before inserting a new node: "))
InsertSpecificItem(start, item)
Traverse(start)
item = int(input("Enter the node which you want to delete: "))
DeleteSpecificItem(start, item)
Traverse(start)
pos = int(input("Enter position where you want to insert a new node: "))
InsertAtPos(start, pos)
Traverse(start)
pos = int(input("Enter postion where you want to delete a node: "))
DeleteAtPos(start, pos)
Traverse(start)
