import pyperf

from graph_builder.GraphBuilder import GraphBuilder
from subway_patrol.SubwayPatrol import SubwayPatrol


def buildGraph():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    return GraphBuilder.build(pathToStations, pathToConnections)


def main():
    functions = [
        SubwayPatrol.travellingSalesmanProblem
    ]

    values = [
        [11],
        [15, 32],
        [13, 75, 100],
        [16, 4, 121, 111],
        [14, 5, 131, 95, 86],
    ]

    g = buildGraph()

    runner = pyperf.Runner()
    for func in functions:
        for value in values:
            record = f'{func.__name__}-{value}'
            runner.bench_func(record, func, g, value)


if __name__ == "__main__":
    main()
