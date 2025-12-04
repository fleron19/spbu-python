from DFS import Graph

def test_graph_iteration():
    g1 = Graph([0, 1, 2, 3, 4, 5, 6, 7],
            [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (3, 7)])
    g1l = list(g1)
    correct_way = [0, 1, 4, 5, 2, 6, 3, 7]
    assert correct_way == g1l

def test_line_iteration():
    g2 = Graph([0, 1, 2, 3, 4],
            [(0, 1), (1, 2), (3, 4)])
    g2l = list(g2)
    correct_way = [0, 1, 2, 3, 4]
    assert correct_way == g2l

def test_single_vertex():
    g3 = Graph([0],
            [])
    g3l = list(g3)
    assert g3l == [0]

def test_zero_vertex():
    g4 = Graph([],
            [])
    g4l = list(g4)
    assert g4l == []

def test_dfs():
    g5 = Graph([0, 1, 2, 3, 4, 5, 6, 7],
            [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (3, 7)])
    correct_way = [0, 1, 4, 5, 2, 6, 3, 7]
    assert correct_way == g5.dfs()







