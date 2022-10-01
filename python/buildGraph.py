import csv
import random

from sqlalchemy import true
from python.graph import Graph
from python.util import Util
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

    def buildRandomGraph(amount_of_nodes, degree, uniform = true):
        g = Graph()
        # Crate vertices
        for i in range(1, amount_of_nodes + 1):
            g.add_station(i, 51 + random.random(), -random.random(),
                          Util.nameGenerator(), random.randint(1, 5))

        # Doesn't add edges if there aren't any other vertices
        # to connect to 
        if amount_of_nodes < 2:
            return g

        # Add edges 
        for i in g.graph:
    
            if uniform:
                # Keep adding edges till degree is met
                while len(g.graph[i].connections) != degree:
                    # First seek out other vertices missing connections
                    for j in g.graph:
                        # Make sure it isn't the same vertice as itself
                        if j != i and len(g.graph[j].connections) != degree:
                            # Generate random line and edge weight
                            line = random.randint(1,4)
                            edge_weight = random.randint(1,3)
                            g.add_line(i, j, line, edge_weight)
                            g.add_line(j, i, line, edge_weight)

                        # Break if i has enough connections
                        if len(g.graph[i].connections) == degree:
                            break
                    
                    # Runs if every node has enough connections already
                    if len(g.graph[i].connections) != degree:
                        # Makes connections with random vertices till it has enough
                        while len(g.graph[i].connections) != degree:
                            random_station = random.randint(1, amount_of_nodes)
                            # Make sure it isn't the same vertice as itself
                            if random_station != i:
                                line = random.randint(1,4)
                                edge_weight = random.randint(1,3)
                                g.add_line(i, random_station, line, edge_weight)
                                g.add_line(random_station, i, line, edge_weight)
            
            # Non uniform distribution
            # Each vertice makes the required amount of connections to a random node
            else:
                while len(g.graph[i].connections) != degree:
                    random_station = random.randint(1,amount_of_nodes)
                    if random_station != i:
                        line = random.randint(1,4)
                        edge_weight = random.randint(1,3)
                        g.add_line(i, random_station, line, edge_weight)
                        g.add_line(random_station, i, line, edge_weight)

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
