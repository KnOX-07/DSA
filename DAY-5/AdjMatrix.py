class AdjMatrix :
    def __init__(self, size):
        self.matrix = [[0]*size for i in range(size)]

    def undirectedEdges(self, start, end):
        self.matrix[start][end] = 1
        self.matrix[end][start] = 1
    
    def directedEdges(self, start, end):
        self.matrix[start][end] = 1

    def edgeUndirectedConnect(self, number) :
        for i in range(number):
            start = int(input("Enter the start node: "))
            end = int(input("Enter the end node: "))
            self.undirectedEdges(start, end)

    def edgeDirectedConnect(self, number):
        for i in range(number) :
            start = int(input("Enter the start node: "))
            end = int(input("Enter the end node: "))
            self.directedEdges(start, end)

    def display(self):
        print("[")
        for row in self.matrix:
            print(row,",")
        print("]")

    def degreeUndirected(self, vertex) :
        count = 0
        for i in range(size):
            if self.matrix[vertex][i] == 1 :
                count += 1
        return count
    def degreeDirected(self, vertex) :
        count = 0
        for i in range(size):
            if self.matrix[vertex][i] == 1:
                count+=1
        return count

size = int(input("Size of the matrix: "))
arr = AdjMatrix(size)
edge = int(input("How many edges do you have? "))
graph = input("Type of the graph(Directed/Undirected): ")
if graph == "Undirected":
    arr.edgeUndirectedConnect(edge)
    print("Degree of vertex 1 is: ",arr.degreeUndirected(1))
    arr.display()
if graph == "Directed":
    arr.edgeDirectedConnect(edge)
    print("Degree of vertex 1 is: ",arr.degreeDirected(1))
    arr.display()
