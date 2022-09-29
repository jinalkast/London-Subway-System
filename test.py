from solution.shortestPath import PathFactory
from solution.graph import Graph, Node
from solution.buildGraph import GraphBuilder
from solution.planning import connectedComponents
from solution.metricsExtraction import MetricsExtractor

def buildGraph():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    return GraphBuilder.build(pathToStations, pathToConnections)

def testMetricsExtractor(g):
    # print("Avg degree for each node = {}\n".format(
    #     MetricsExtractor.compute_avg_degree(g.graph)))

    # print("computing which stations are in which zone...")

    assert MetricsExtractor.compute_avg_degree(g.graph) == 2.6887417218543046
    num_of_stations_in_zone= {3:64,1:60,2:96,4:44,5:28,6:20,7:3,10:2,9:1,8:2}
    zone_list = MetricsExtractor.return_zone_list(g.graph)
    for zone in zone_list:
        assert (len(zone_list[zone])) == num_of_stations_in_zone[zone]


def testShortestPath(g):
    #print("Using Djikstras for path 9-302")
    itinerary = PathFactory.dijkstra(g, 110, 190)
    assert itinerary.path == [[110, 2.0, 10], [265, 3.0, 10], [1, 4.0, 10], [234, 1.0, 10], [176, 2.0, 10], [30, 3.0, 10]]

    #print("Using A* for path 9-302")
    itinerary2 = PathFactory.a_star(g, 110, 190)
    assert itinerary2.path == [[110, 2.0, 10], [265, 3.0, 10], [1, 4.0, 10], [234, 1.0, 10], [176, 2.0, 10], [30, 3.0, 10]]

    #print("Using Djikstras for path 11-163")
    itinerary3 = PathFactory.dijkstra(g, 11, 163)
    assert itinerary3.path == [[11, 1.0, 1]]

    #print("Using A* for path 11-163")
    itinerary4 = PathFactory.a_star(g, 11, 163)
    assert itinerary4.path == [[11, 1.0, 1]]

    #print("Using Djikstras for path 11-82")
    itinerary5 = PathFactory.dijkstra(g, 11, 82)
    assert itinerary5.path  == [[11, 1.0, 1], [163, 2.0, 1]]

    #print("Using A* for path 11-82")
    itinerary6 = PathFactory.a_star(g, 11, 82)
    assert itinerary6.path == [[11, 1.0, 1], [163, 2.0, 1]]

def testCC(g):
    g.zone_list = MetricsExtractor.return_zone_list(g.graph)
    g.cc = connectedComponents.returnCC(g.graph, g.zone_list)
    connectedComponents.printCC(g.cc)

g = buildGraph()
testMetricsExtractor(g)
#testShortestPath(g)
#testCC(g)