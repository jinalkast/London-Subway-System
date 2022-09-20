import csv
from solution.graph import Graph, Node


class GraphBuilder():
    def build(pathToStations, pathToConnections, directed=False):
        g = Graph()
        with open(pathToStations) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)
            for row in csvReader:
                g.graph[int(row[0])] = Node(float(row[1]), float(
                    row[2]), row[3])

        with open(pathToConnections) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)

            if directed:

                for row in csvReader:
                    # Source Destination, Line, Edge weight
                    g.graph[int(row[0])].connections.append(
                        [int(row[1]), int(row[2]), float(row[3])])

            else:
                for row in csvReader:
                    g.graph[int(row[0])].connections.append(
                        [int(row[1]), int(row[2]), float(row[3])])
                    g.graph[int(row[1])].connections.append(
                        [int(row[0]), int(row[2]), float(row[3])])
        return g
