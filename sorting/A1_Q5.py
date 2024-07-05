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
        print("The List is:", self.a)
        
    def InsertionSort(self):
        for j in range(1, self.size):
            item = self.a[j]
            pos = j-1
            while item<self.a[pos] and pos>=0:
                self.a[pos+1] = self.a[pos]
                pos-=1
            self.a[pos+1] = item
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
ob1.InsertionSort()
ob1.display()
ob1.insert(51)
ob1.delete(45)