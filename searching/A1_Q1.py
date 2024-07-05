class LinearList:
    def __init__(self, a, d1):
        self.a = a
        self.size = len(a)
        self.data = d1
        
        for i in self.a:
            if type(i)!= d1:
                print("The element should be an integer")
                exit()
    def display(self):
        print("List:", self.a)
        
    def LinearSearch(self,item):
        for i in range(self.size):
            if item == self.a[i]:
                return 1
        return -1
        
    def insert(self, e):
        self.a.append(e)
        print("After inserting:", self.a)
    def delete(self, e):
        self.a.remove(e)
        print("After deleting:", self.a)
                     
ob1 = LinearList([2, 6, 5, 10, 17, 15], int)
ob1.LinearSearch(5)
ob1.display()
ob1.insert(27)
ob1.delete(17)
