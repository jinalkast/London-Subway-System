from solution.shortestPath import *
from solution.graph import Graph, Node
from solution.buildGraph import GraphBuilder
from solution.planning import *
from solution.metricsExtraction import MetricsExtractor


def main():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)
    # print(compute_sum_of_degrees(g))
    # PathCalculator.a_star(g, 11, 283)
    # print()
    itinerary = PathFactory.dijkstra(g, 9, 302)
    itinerary.printPath()
    # print(g.graph[2].zone)
    g.zone_list = MetricsExtractor.return_zone_list(g.graph)
    #g.cc = connectedComponents.returnCC(g.graph, g.zone_list)
    #cov bnnnectedComponents.printCC(g.cc)

main()
