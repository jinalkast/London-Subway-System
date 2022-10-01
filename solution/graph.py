# Node class used by graph
class Node():
    def __init__(self, lat, long, name, zone) -> None:
        self.lat = lat
        self.long = long
        self.name = name
        self.connections = []
        self.zone = zone


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


class Itinerary():
    def __init__(self, parent_list, start, finish):
        self.start = start
        self.finish = finish
        self.path = self.compute_path(parent_list)

    # Computes route given parent list
    def compute_path(self, parent_list):
        path = []
        i = self.finish

        # Go through parent list until you reach src
        while parent_list[i][0] != i:
            path.append(parent_list[i])
            i = parent_list[i][0]

        # Reverse list
        return path[::-1]

    def printPath(self):
        i = 0
        while i < (len(self.path)):
            # Keep track of total # of stops
            stops = self.path[i][1]

            # Paths of length == 2 infinite loop without this line
            if i + 1 == len(self.path):
                print("Go from {} to {} in {} stops using line {}".format(
                    self.path[i][0], self.finish, stops, self.path[i][2]
                ))
                i += 1

            # Find when line is switched
            for j in range(i + 1, len(self.path)):
                # Line is switched
                if self.path[j][2] != self.path[i][2]:
                    print("Go from {} to {} in {} stops with line {}".format(
                        self.path[i][0], self.path[j][0], stops, self.path[i][2]
                    ))
                    i = j
                    break

                # Reached end without switching lines
                elif j == len(self.path) - 1:
                    print(
                        "Go from {} to {} in {} stops using line {}".format(
                            self.path[i][0],
                            self.finish,
                            stops + self.path[j][1],
                            self.path[i][2]))
                    i = j + 1
                    break

                # Num of stops accumulates
                stops += self.path[j][1]
