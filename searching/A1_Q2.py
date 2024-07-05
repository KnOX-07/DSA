class BinaryList:
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
        
    def BinarySearch(self,item):
        beg = 0
        end = self.size
        f = 0
        while beg <= end:
            mid = (beg+end)//2
            if self.a[mid]==item:
                f = 1
                break
            elif self.a[mid]<item:
                beg = mid+1
            else:
                end = mid-1
        if f == 1:
            print("Item found at index", mid)
        else:
            print("Item not found")
        
    def insert(self, e):
        self.a.append(e)
    def delete(self, e):
        self.a.remove(e)
            
#ob1 = BinaryList([10, 20, 30, 45, 60], int)
l = [10, 20, 30, 45, 60]
ob1 = BinaryList(l, int)
ob1.display()
ob1.BinarySearch(20)