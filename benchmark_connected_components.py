import pyperf

from python.buildGraph import GraphBuilder
from python.metricsExtraction import MetricsExtractor
from python.connectedComponents import connectedComponents


def buildGraph():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    return GraphBuilder.build(pathToStations, pathToConnections)


def main():
     g = buildGraph()
     zone_list = MetricsExtractor.return_zone_list(g)
     cc = connectedComponents.returnCC(g,zone_list)
     runner = pyperf.Runner()


     runner.bench_func("Finding Connected Components",
                         connectedComponents.returnCC, g,zone_list)
     runner.bench_func("Finding Crossing Edges between zones",
                         connectedComponents.generateCrossingEdgesBetweenZones, g)
     runner.bench_func("Generating Components graph", GraphBuilder.buildComponentGraph, g, cc)

    
if __name__ == "__main__":
    main()