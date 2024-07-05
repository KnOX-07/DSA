class LinearList:
    def __init__(self, a, d1):
        self.a = a
        self.size = len(a)
        self.data = d1
        
        for i in self.a:
            if type(i)!= int:
                print("The element should be an integer")
                exit()
    def display(self):
        print("List:", self.a)
        
    def BubbleSort(self):
        for i in range(1, self.size):
            for k in range(0, self.size-1):
                if self.a[k]>self.a[k+1]:
                    self.a[k],self.a[k+1] = self.a[k+1], self.a[k]
        print("The sorted array is:", self.a)
        
    def insert(self, e):
        self.a.append(e)
        print("After inserting:", self.a)
    def delete(self, e):
        for i in self.a:
            if e not in self.a:
                print("Item does not exist")
        self.a.remove(e)
        print("After deleting:", self.a)
            
            
ob1 = LinearList([50, 30, 40, 45, 65, 68, 120, 170], int)
ob1.BubbleSort()
ob1.display()
ob1.insert(51)
ob1.delete(45)