class Node:
    def __init__(self,value):
        self.prev = None
        self.info = value
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.start = None

    def InsertAtEnd(self,v):
        n = Node(v)
        if self.start == None:
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
            n.prev = temp
    
    def InsertAtBeg(self,v):
        n = Node(v)
        temp = self.start
        temp.prev = n
        n.next = temp
        n.prev = None
        self.start = n

    def InsertAfterSpecificItem(self,item):
        v = int(input())
        n = Node(v)
        temp = self.start
        while temp.info != item:
            temp = temp.next
        var = temp.next
        n.next = temp.next
        n.prev = temp
        temp.next = n
        var.prev = n
        

    def InsertAtPosition(self,pos):
        return

    def DeleteBeg(self):
        temp = self.start
        new = temp.next
        new.prev = None
        self.start = new
        del temp

    def DeleteEnd(self):
        temp = self.start
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp   
        
    
    def traverse(self):
        temp = self.start
        while temp != None:
            print(temp.info)
            temp = temp.next

DLL = DoubleLinkedList()
DLL.InsertAtEnd(50)
DLL.InsertAtEnd(100)
DLL.InsertAtEnd(150)
DLL.InsertAtBeg(20)
DLL.InsertAtBeg(90)
DLL.DeleteBeg()
DLL.DeleteEnd()
DLL.InsertAfterSpecificItem(50)
DLL.traverse()
