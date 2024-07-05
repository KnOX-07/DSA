class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        
    def InsertAtLast(self, v):
        n = Node(v)
        if self.start == None:
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
            
    def ReverseList(self):
        prev = self.start
        cur = prev.next
        next_node = cur.next
        while cur.next != None:
            cur.next = prev
            prev = cur
            cur = next_node
            next_node = next_node.next
        self.start.next = None
        cur.next = prev
        self.start = cur

    def Traverse(self):    
        n = self.start
        while n != None:
            print(n.info, end=" ⇢ ")
            n = n.next
        print("None")

l1 = LinkedList()
l1.InsertAtLast(12)
l1.InsertAtLast(24)
l1.InsertAtLast(55)
l1.Traverse()
print("═══════════════════")
l1.ReverseList()
l1.Traverse()