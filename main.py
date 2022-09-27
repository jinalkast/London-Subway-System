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
    print("Avg degree for each node = {}\n".format(
        MetricsExtractor.compute_avg_degree(g.graph)))

    print("computing which stations are in which zone...")

    zone_list = MetricsExtractor.return_zone_list(g.graph)
    for zone in zone_list:
        print("Zone {} has stations: ".format(zone))
        print(zone_list[zone])

    # PathFactory.a_star(g, 11, 283)
    # print()


def testShortestPath(g):
    # print("Using Djikstras for path 9-302")
    # itinerary = PathFactory.dijkstra(g, 9, 302)
    # itinerary.printPath()
    # print()

    print("Using A* for path 9-302")
    itinerary2 = PathFactory.a_star(g, 9, 302)
    itinerary2.printPath()
    print()

    # print("Using Djikstras for path 11-163")
    # itinerary3 = PathFactory.dijkstra(g, 11, 163)
    # itinerary3.printPath()
    # print()

    # print("Using A* for path 11-163")
    # itinerary4 = PathFactory.a_star(g, 11, 163)
    # itinerary4.printPath()
    # print()

    # print("Using Djikstras for path 11-82")
    # itinerary5 = PathFactory.dijkstra(g, 11, 82)
    # itinerary5.printPath()
    # print()

    # print("Using A* for path 11-82")
    # itinerary6 = PathFactory.a_star(g, 11, 82)
    # itinerary6.printPath()
    # print()

def testCC(g):
    g.zone_list = MetricsExtractor.return_zone_list(g.graph)
    g.cc = connectedComponents.returnCC(g.graph, g.zone_list)
    connectedComponents.printCC(g.cc)

g = buildGraph()
#testMetricsExtractor(g)
testShortestPath(g)
#testCC(g)