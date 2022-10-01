from solution.buildGraph import GraphBuilder


def test_buildGraph():
     pathToStations = "_dataset/london.stations.csv"
     pathToConnections = "_dataset/london.connections.csv"
     g = GraphBuilder.build(pathToStations, pathToConnections)

     assert len(g.graph) == 302
     assert (len(g.graph[11].connections) == 10)

test_buildGraph()