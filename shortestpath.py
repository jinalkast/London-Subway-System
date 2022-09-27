import csv
from collections import defaultdict
from math import radians, cos, sin, asin, sqrt
import time


# Simple priority Queue
# removeMin runs in O(n) time complexity
class PriorityQueue():
    def __init__(self):
        # Queue is a dictionary to support any station having any unique id
        self.queue = {}

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, id, dist):
        self.queue[id] = dist

    def changeVal(self, id, val):
        self.queue[id] = val

    def removeMin(self):
        minVal = 1e7
        minIndex = -1
        for i in self.queue:
            if self.queue[i] < minVal:
                minVal = self.queue[i]
                minIndex = i

        del self.queue[minIndex]
        return [minIndex, minVal]


class node():
    def __init__(self, lat, long, name, zone, total_lines, hasRail) -> None:
        self.lat = lat
        self.long = long
        self.name = name
        self.zone = zone  # Could be removed
        self.total_lines = total_lines  # Could be removed
        self.hasRail = (1 == hasRail)  # Could be removed
        self.connections = []


class Graph():
    def __init__(self):
        self.graph = {}
        self.parent = {}
        self.fresh = False  # Is True when running Djikstras and goes to false
        # When you update a value in the graph

    def add_station(self, id, lat, long, name, zone, total_lines, hasRail):
        # Because this command is manual it assumes correct datatypes
        # Also this works as an override
        self.graph[id] = node(id, lat, long, name, zone, total_lines, hasRail)
        self.fresh = False

    def add_line(self, src, dest, line, weight, directed=False):
        if directed:
            self.graph[src].connections.append([dest, line, weight])

        else:
            self.graph[src].connections.append([dest, line, weight])
            self.graph[dest].connections.append([src, line, weight])
        self.fresh = False

    def build_graph(self, pathToStations, pathToConnections, directed=False):

        with open(pathToStations) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)
            for row in csvReader:
                self.graph[int(row[0])] = node(float(row[1]), float(
                    row[2]), row[3], float(row[5]), int(row[6]), int(row[7]))

        with open(pathToConnections) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            next(csvReader)

            if directed:

                for row in csvReader:
                    # Source Destination, Line, Edge weight
                    self.graph[int(row[0])].connections.append(
                        [int(row[1]), int(row[2]), float(row[3])])

            else:
                for row in csvReader:
                    self.graph[int(row[0])].connections.append(
                        [int(row[1]), int(row[2]), float(row[3])])
                    self.graph[int(row[1])].connections.append(
                        [int(row[0]), int(row[2]), float(row[3])])

        self.fresh = False


def compute_avg_degree(graph):
    num_of_edges = sum(len(node.connections)
                       for node in graph.graph.values())
    return (num_of_edges / len(graph.graph))


def compute_sum_of_degrees(graph):
    degreesCount = defaultdict(lambda: 0)

    for i in graph.graph.values():
        degreesCount[len(i.connections)] += 1

    return degreesCount


def dijkstra(graph, src, dest):
    if not (graph.fresh):
        graph.fresh = True  # set it so that the information
        # is updated
        dist = {}   # dist values used to pick minimum
        # weight edge in cut

        graph.parent = {}
        graph.parent[src] = [src, 0, 0]
        # minHeap represents set E
        pQueue = PriorityQueue()

        # Initialize min heap with all vertices.
        # dist value of all vertices
        for id in graph.graph:
            dist[id] = 1e7
            pQueue.insert(id, 1e7)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        pQueue.changeVal(src, 0)
        dist[src] = 0

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while pQueue.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newPqueueNode = pQueue.removeMin()
            u = newPqueueNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for neighbour in graph.graph[u].connections:

                neighbourID = neighbour[0]
                line = neighbour[1]
                neighbourDist = neighbour[2]

                # Recalculate shortest distance
                if (
                        neighbourID in pQueue.queue and
                        dist[u] != 1e7 and
                        neighbourDist + dist[u] < dist[neighbourID]):

                    dist[neighbourID] = neighbourDist + dist[u]
                    graph.parent[neighbourID] = [u, neighbourDist, line]
                    # update distance value
                    # in min heap also
                    pQueue.changeVal(neighbourID, dist[neighbourID])

    # Print shortest path
    printShortestPath(graph,src,dest)


def a_star(graph, src, dest):

    def hScore(src, dest):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(graph.graph[src].long)
        lon2 = radians(graph.graph[dest].long)
        lat1 = radians(graph.graph[src].lat)
        lat2 = radians(graph.graph[dest].lat)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r)

    graph.parent = {}
    graph.parent[src] = [src, 0, 0]
    pQueue = PriorityQueue()

    gScore = {}
    fScore = {}

    for id in graph.graph:
        gScore[id] = 1e7
        fScore[id] = 1e7
        pQueue.insert(id, 1e7)

    pQueue.changeVal(src, 0)
    gScore[src] = 0
    fScore[src] = 0

    while pQueue.isEmpty() == False:

        pQueueNode = pQueue.removeMin()
        current = pQueueNode[0]

        for neighbour in graph.graph[current].connections:
            neighbourID, line, neighbourDist = neighbour[0], neighbour[1], neighbour[2]

            temp_gScore = gScore[current] + neighbourDist

            if temp_gScore < gScore[neighbourID]:
                gScore[neighbourID] = temp_gScore
                fScore[neighbourID] = temp_gScore + \
                    hScore(current, neighbourID)
                graph.parent[neighbourID] = [
                    current, neighbourDist, line]

                if neighbourID in pQueue.queue:
                    pQueue.changeVal(neighbourID, fScore[neighbourID])

    # Print shortest path
    printShortestPath(graph,src,dest)

def printShortestPath(graph,src,dest):
    # Print shortest path
    msg = []
    i = dest

    while graph.parent[i][0] != src:
        #start_station = graph.graph[graph.parent[i][0]].name
        #parents_parent = graph.parent[i].parent
        #while graph.parent[i][0].parent!= src and graph.parent[i][2] == graph.parent[i][0].parent[graph.parent[i]][2]:
        #    i = graph.parent[i][0]
        msg.append("Go from {} to {} using line {} for {} stops".format(
            graph.graph[graph.parent[i][0]].name, graph.graph[i].name, graph.parent[i][2], graph.parent[i][1]))
        i = graph.parent[i][0]
    msg.append("Go from {} to {} using line {} for {} stops".format(
        graph.graph[graph.parent[i][0]].name, graph.graph[i].name, graph.parent[i][2], graph.parent[i][1]))

    for i in range(len(msg) - 1, -1, -1):
        print(msg[i])

def main():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = Graph()
    g.build_graph(pathToStations, pathToConnections)
    a_star_start = time.time()
    a_star(g, 11, 283)
    a_star_end = time.time()
    print()
    djikstra_start = time.time()
    dijkstra(g, 11, 283)
    djikstra_end = time.time()
    print("------------------------")
    a_star_time = 1000 * (a_star_end - a_star_start)
    djikstra_time = 1000 * (djikstra_end - djikstra_start)
    print("A* time: " + str(round(a_star_time, 3)) + "ms")
    print("Djikstra time: " + str(round(djikstra_time, 3)) + "ms")
    # print(compute_avg_degree(g))

main()