class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.ind = 0

    def dfs_gen(self):
        states = {"white": [v for v in self.vertices], "gray": list(), "black": list()}
        visited_verteces = []

        def dfs_step(vertex):
            if vertex in states["white"]:
                states["gray"].append(vertex)
                states["white"].remove(vertex)
                visited_verteces.append(vertex)
                for edge in self.edges:
                    if edge[0] == vertex:
                        dfs_step(edge[1])
                    if edge[1] == vertex:
                        dfs_step(edge[0])

        for vertex in self.vertices:
            dfs_step(vertex)
        yield from visited_verteces
    
    def __iter__(self):
        return self.dfs_gen()
    
    # realisation of dfs method that returns list of visited verteces (first subtask)
    def dfs(self): 
        return list(self.dfs_gen())
    

