class LinearList:
    def __init__(self, a, d1):
        self.a = a
        self.size = len(self.a)
        for i in self.a:
            if type(i) != d1:
                print("The element should be an integer")
                exit()

    def display(self):
        print("The List is:",self.a)

    def partition(self, low, high):
        piv = self.a[low]
        i = low
        j = high
        while i < j:
            while self.a[i] <= piv and i < high:
                i += 1
            while self.a[j] > piv and j > low:
                j -= 1
            if i < j:
                self.a[i], self.a[j] = self.a[j], self.a[i]
        self.a[low], self.a[j] = self.a[j], self.a[low]
        return j

    def QuickSort(self, low, high):
        if low < high:
            pindex = self.partition(low, high)
            self.QuickSort(low, pindex - 1)
            self.QuickSort(pindex + 1, high)
        return self.a
    
    def insert(self, item):
        self.a.append(item)
        self.size += 1
        print("After inserting:", self.a)
    def delete(self, item):
        for i in self.a:
            if item not in self.a:
                print("Item does not exist")
        self.a.remove(item)
        print("After deleting:", self.a)
            
arr = [50, 30, 40, 65, 45, 68, 120, 170]
ob1 = LinearList(arr, int)
ob1.QuickSort(0, len(arr)-1)
ob1.display()
ob1.insert(24)
ob1.insert(51)
ob1.delete(24)