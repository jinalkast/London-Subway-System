from python.buildGraph import GraphBuilder
from python.PriorityQueue import PriorityQueue
from python.shortestPath import PathFactory
from python.metricsExtraction import MetricsExtractor
from python.planning import connectedComponents
from python.util import Util

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


def test_priorityQueue():
    q = PriorityQueue()

    q.insert(3, 1)
    assert (q.removeMin() == [3, 1])

    for i in [[10, 10], [9, 1], [3, -5000]]:
        q.insert(i[0], i[1])

    assert (q.removeMin() == [3, -5000])


def test_shortest_path():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)

    itineray1 = PathFactory.dijkstra(g, 11, 283)
    itineray2 = PathFactory.a_star(g, 11, 283)
    itineray3 = PathFactory.dijkstra(g, 43, 165)
    itineray4 = PathFactory.a_star(g, 43, 165)
    itineray5 = PathFactory.dijkstra(g, 1, 2)
    itineray6 = PathFactory.a_star(g, 1, 2)

    assert (itineray1.path == [[11, 1.0, 1], [163, 2.0, 1], [82, 3.0, 1],
                               [193, 1.0, 6], [218, 2.0, 6]])

    assert (itineray2.path == [[11, 1.0, 1], [163, 2.0, 1],
                               [82, 3.0, 1], [193, 1.0, 6], [218, 2.0, 6]])

    assert (itineray3.path == [[43, 3.0, 7], [289, 2.0, 4], [36, 2.0, 4],
                               [33, 1.0, 4], [164, 2.0, 2], [24, 3.0, 2],
                               [156, 2.0, 3], [167, 1.0, 9], [188, 3.0, 9],
                               [7, 2.0, 9], [145, 2.0, 9], [89, 3.0, 9],
                               [40, 2.0, 9], [139, 2.0, 9], [264, 2.0, 9],
                               [8, 3.0, 9], [124, 2.0, 9], [77, 4.0, 9],
                               [93, 3.0, 9]])

    assert (itineray4.path == [[43, 3.0, 7], [289, 2.0, 4], [36, 2.0, 4],
                               [33, 1.0, 4], [164, 2.0, 2], [24, 3.0, 2],
                               [156, 2.0, 3], [167, 1.0, 9], [188, 3.0, 9],
                               [7, 2.0, 9], [145, 2.0, 9], [89, 3.0, 9],
                               [40, 2.0, 9], [139, 2.0, 9], [264, 2.0, 9],
                               [8, 3.0, 9], [124, 2.0, 9], [77, 4.0, 9],
                               [93, 3.0, 9]])

    assert (itineray5.path == [[1, 3.0, 10], [265, 2.0, 10], [110, 1.0, 4],
                               [17, 3.0, 10], [74, 2.0, 10], [99, 1.0, 3],
                               [236, 2.0, 3], [229, 2.0, 3], [273, 2.0, 3],
                               [248, 2.0, 3], [285, 2.0, 7], [279, 4.0, 12],
                               [13, 2.0, 2], [156, 2.0, 3]])

    assert (itineray6.path == [[1, 3.0, 10], [265, 2.0, 10], [110, 1.0, 4],
                               [17, 3.0, 10], [74, 2.0, 10], [99, 1.0, 3],
                               [236, 2.0, 3], [229, 2.0, 3], [273, 2.0, 3],
                               [248, 2.0, 3], [285, 2.0, 7], [279, 4.0, 12],
                               [13, 2.0, 2], [156, 2.0, 3]])

    #print(itineray1.total_path_length)

def test_conected_components():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)

    g.zone_list = MetricsExtractor.return_zone_list(g)
    g.cc = connectedComponents.returnCC(g, g.zone_list)
   
    assert(g.cc[8] == [[280], [53]])
    assert(g.cc[9] == [[46]])
    assert(g.cc[10] == [[50], [6]])

# test_buildGraph()
# test_priorityQueue()
# test_shortest_path()
# test_conected_components()0

# g = GraphBuilder.buildRandomGraph(5,5)
# for i in g.graph:
#     print("Station {} has vertices".format(i))
#     print(g.graph[i].connections)
#     print()
