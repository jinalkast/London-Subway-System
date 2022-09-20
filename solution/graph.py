class Node():
    def __init__(self, lat, long, name) -> None:
        self.lat = lat
        self.long = long
        self.name = name
        self.connections = []


class Graph():
    def __init__(self):
        self.graph = {}
        self.parent = {}
        self.fresh = False  # Is True when running Djikstras and goes to false
        # When you update a value in the graph

    def add_station(self, id, lat, long, name):
        # Because this command is manual it assumes correct datatypes
        # Also this works as an override
        self.graph[id] = Node(id, lat, long, name)
        self.fresh = False

    def add_line(self, src, dest, line, weight, directed=False):
        if directed:
            self.graph[src].connections.append([dest, line, weight])

        else:
            self.graph[src].connections.append([dest, line, weight])
            self.graph[dest].connections.append([src, line, weight])
        self.fresh = False
