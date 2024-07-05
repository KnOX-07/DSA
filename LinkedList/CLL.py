class Node:
    def __init__(self,value):
        self.info = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.start = None
    
    def InsertAtEnd(self,value):
        n = Node(value)
        if self.start == None:
            self.start = n
            n.next = self.start
        else:
            n = Node(value)
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = n
            n.next = self.start
    
    def InsertAtBeg(self,v):
        new = Node(v)
        if self.start == None:
            self.start = new
            new.next = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            new.next = self.start
            self.start = new
            temp.next = self.start

    def InsertAfterSpecificItem(self,item):
        value = int(input())
        new = Node(value)
        temp = self.start
        while temp.info != item:
            temp = temp.next
        new.next = temp.next
        temp.next = new


    def InsertAtPos(self,pos):
        temp = self.start
        v = int(input())
        n = Node(v)
        for i in range(1,pos-1):
            temp = temp.next
        n.next = temp.next
        temp.next = n

    def DeleteLastNode(self):
        temp = self.start
        while temp.next != self.start:
            prev = temp
            temp = temp.next
        prev.next = self.start
        del temp
    
    def DeleteFirstNode(self):
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        var = self.start
        self.start = var.next
        temp.next = self.start
        del var

    def DeleteSpecificItem(self,item):
        temp = self.start
        while temp.info != item:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp
        
    
    def traverse(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.info, end= "-->")
            temp = temp.next
        print(temp.info)


CLL = CircularLinkedList()
CLL.InsertAtEnd(98)
CLL.InsertAtEnd(99)
CLL.InsertAtEnd(100)
CLL.InsertAtEnd(101)
CLL.InsertAtEnd(102)
CLL.InsertAfterSpecificItem(101)
#CLL.DeleteSpecificItem(100)
CLL.InsertAtPos(3)
CLL.traverse()
