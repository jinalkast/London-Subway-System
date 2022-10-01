import pyperf

from python.buildGraph import GraphBuilder
from python.shortestPath import PathFactory

def buildGraph():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    return GraphBuilder.build(pathToStations, pathToConnections)

def main():
    functions = [
        PathFactory.a_star,
        PathFactory.dijkstra
    ]

    values = [
        [11, 163], #1 connection, same line (0 line changes)
        [49, 279], #2 connections, same line
        [263, 161], #3 connections, same line
        [263, 25], #4 connections, same line
        [285, 99], #5 connections, same line
        [110, 190], #6 connections, same line
        [28, 277], #1 line change
        [49, 254], #2 line changes
        [56, 114], #3 line changes
        [37, 17], #4 line changes
        [37, 110] #5 line changes
    ]

    g = buildGraph()

    runner = pyperf.Runner()
    for func in functions:
        for valuePair in values:
            record = f'{func.__name__}-{valuePair}'
            runner.bench_func(record, func, g, valuePair[0], valuePair[1])
    
if __name__ == "__main__":
    main()