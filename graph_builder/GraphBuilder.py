import csv
import random
from graph.Graph import Graph
from util.Util import Util
from collections import defaultdict


class GraphBuilder():

    def build(pathToStations, pathToConnections, directed=False):
        g = Graph()

        # Read stations csv file, add node to graph for each station
        with open(pathToStations) as csvfile:
            # Initialize the reader and skip the first column containing
            # column headers
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)

            # read through remaining columns
            for row in csvReader:
                # Format of add station is:
                # ID, Latitude, Longitude, name, zone
                g.add_station(
                    int(row[0]), float(row[1]), float(row[2]),
                    row[3], float(row[5]))

        # Read connections csv file and add edge to graph for each station
        with open(pathToConnections) as csvfile:
            # Initialize the reader and skip the first column containing
            # column headers
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)

            # Add two edges if undirected. Assumes undirected by default
            if directed:
                for row in csvReader:
                    # Format of add_line is
                    # src, dest, line, edge weight
                    g.add_line(int(row[0]), int(row[1]),
                               int(row[2]), float(row[3]))

            else:
                for row in csvReader:
                    # Format of add_line is
                    # src, dest, line, edge weight
                    g.add_line(int(row[0]), int(row[1]),
                               int(row[2]), float(row[3]))
                    g.add_line(int(row[1]), int(row[0]),
                               int(row[2]), float(row[3]))
        return g

    def buildComponentGraph(graph, connectedComponents):
        cc = connectedComponents
        graph_of_components = Graph()

        # Maps vertex to corresponding component
        componentsHolding = defaultdict(list)
        i = 0
        # Create vertices
        for zone in cc:
            for component in cc[zone]:
                graph_of_components.add_station(i, 0, 0, str(i), zone)
                for node in component:
                    componentsHolding[node].append(i)
                i += 1

        # Add edges
        i = 0
        for zone in cc:
            for component in cc[zone]:
                for node in component:
                    for neighbour in graph.graph[node].connections:
                        for component_dest in componentsHolding[neighbour[0]]:
                            if component_dest != i:
                                # Add line from component i to all components
                                # holding a neigbour to component i
                                graph_of_components.add_component_edge(
                                    i, component_dest, node, neighbour[0])
                i += 1

        return [componentsHolding, graph_of_components]
