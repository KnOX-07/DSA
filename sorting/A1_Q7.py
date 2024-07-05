class LinearList:
    def __init__(self):
        self.a = []

    def insert(self, e):
        self.a.append(e)
        print("Array after inserting:", self.a)

    def delete(self, e):
        if e not in self.a:
            print("Item does not exist!")
            return
        self.a.remove(e)
        print("Array after deleting:", self.a)

    def mergeSort(self, b):
        a = self.a
        i, j = 0, 0
        c = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

        while i < len(a):
            c.append(a[i])
            i += 1

        while j < len(b):
            c.append(b[j])
            j += 1

        print("Sorted array:", c)
        
l1 = LinearList()
l1.insert(5)
l1.insert(20)
l1.insert(79)
l1.insert(12)
l1.insert(54)

l1.mergeSort([50, 30, 40, 45, 65, 68, 120, 170])

l1.delete(20)
l1.delete(100)