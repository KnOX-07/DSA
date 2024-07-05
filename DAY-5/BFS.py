class BFS:
    def __init__(self):
        self.adj = [[0, 1, 1, 1, 0], 
                    [1, 0, 0, 1, 1], 
                    [1, 0, 0, 1, 0], 
                    [1, 1, 1, 0, 1], 
                    [0, 1, 0, 1, 0]]
        print(self.adj)
        self.status = [1 for i in range(len(self.adj))]
        print(self.status)

t = BFS()
