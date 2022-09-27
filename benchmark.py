import pyperf

from solution.buildGraph import GraphBuilder
from solution.shortestPath import PathFactory

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
        [9, 302],
        [11, 163],
        [11, 82]
    ]

    g = buildGraph()

    runner = pyperf.Runner()
    for func in functions:
        for valuePair in values:
            record = f'{func.__name__}-{valuePair}'
            runner.bench_func(record, func, g, valuePair[0], valuePair[1])
    
if __name__ == "__main__":
    main()
