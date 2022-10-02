from graph.Node import Node


class Graph():
    def __init__(self):
        # Graph contains list of nodes
        # Parent contains stored solution to shortest path problem
        self.graph = {}
        self.parent = {}

    def add_station(self, id, lat, long, name, zone):
        # Assumes correct datatypes
        # Also this works as an override
        self.graph[id] = Node(lat, long, name, zone)

    def add_line(self, src, dest, line, weight):
        # Assumes correct datatypes
        # Does not override
        if [dest, line, weight] not in self.graph[src].connections:
            self.graph[src].connections.append([dest, line, weight])

    def add_component_edge(
            self,
            starting_comp,
            ending_comp,
            starting_station,
            ending_station):
        if [ending_comp, starting_station,
                ending_station] not in self.graph[starting_comp].connections:
            self.graph[starting_comp].connections.append(
                [ending_comp, starting_station, ending_station])
