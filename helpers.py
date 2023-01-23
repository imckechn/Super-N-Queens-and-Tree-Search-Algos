def graphInit():
    # [ starting node, heuristic cost, ending node, vertice cost ]
    graph = [
        ['S', 8, 'A', 3],
        ['S', 7, 'C', 5],
        ['S', 9, 'B', 2],
        ['A', 6, 'G', 2],
        ['A', 7, 'C', 3],
        ['G', 3, 'E', 5],
        ['G', 4, 'D', 4],
        ['E', 0, 'F', 5],
        ['H', 8, 'A', 4],
        ['H', 4, 'D', 4],
        ['B', 9, 'A', 4],
        ['B', 8, 'D', 6],
        ['C', 9, 'B', 4],
        ['C', 3, 'H', 3],
        ['D', 0, 'F', 3],
        ['F', 0, '', 0]
    ]

    return graph

#Helper method that returns the weight of the vertice
def getWeight(path):
    return path[3]

#Helper method that returns the weight of the heuristic value
def getHeuristic(path):
    return path[1]