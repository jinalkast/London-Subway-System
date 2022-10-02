from graph_builder.GraphBuilder import GraphBuilder


def test_buildGraph():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)

    assert len(g.graph) == 302
    assert (len(g.graph[11].connections) == 10)
    assert (g.graph[24].lat == 51.527)
    assert (g.graph[24].long == -0.0549)

    thirty_two_neighbours = [70, 204]
    for i in thirty_two_neighbours:
        assert (i in connection for connection in g.graph[32].connections)

    eleven_neighbours = [163, 212, 83, 104, 28, 249, 94, 104]
    for i in eleven_neighbours:
        assert (i in connection for connection in g.graph[11].connections)
