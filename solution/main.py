from shortestPath import *
from graph import Graph,Node
from buildGraph import GraphBuilder
def main():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations,pathToConnections)
    # print(compute_sum_of_degrees(g))
    pathCalculator.a_star(g, 11, 283)
    print()
    pathCalculator.dijkstra(g, 11, 283)
    # print(compute_avg_degree(g))

main()