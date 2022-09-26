class Node():
    def __init__(self, lat, long, name, zone) -> None:
        self.lat = lat
        self.long = long
        self.name = name
        self.connections = []
        self.zone = zone


class Graph():
    def __init__(self):
        self.graph = {}
        self.parent = {}

    def add_station(self, id, lat, long, name, zone):
        # Because this command is manual it assumes correct datatypes
        # Also this works as an override
        self.graph[id] = Node(id, lat, long, name, zone)

    def add_line(self, src, dest, line, weight, directed=False):
        if directed:
            self.graph[src].connections.append([dest, line, weight])

        else:
            self.graph[src].connections.append([dest, line, weight])
            self.graph[dest].connections.append([src, line, weight])


class Itinerary():
    def __init__(self, parent_list, start, finish):
        self.start = start
        self.finish = finish
        self.path = self.compute_path(parent_list)

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
        if len(self.path) == 1:
            print("Go from {} to {} in {} stops using line {}".format(
                self.path[0][0], self.finish, self.path[0][1], self.path[0][2]
            ))
            return

        i = 0
        while i < (len(self.path)):
            stops = self.path[i][1]

            # Find when line is switched
            for j in range(i + 1, len(self.path)):
                # Line is switched
                if self.path[j][2] != self.path[i][2]:
                    print("Go from {} to {} in {} stops using line {}".format(
                        self.path[i][0], self.path[j][0], stops, self.path[i][2]
                    ))
                    i = j
                    break

                # Reached end without switching lines
                elif j == len(self.path) - 1:
                    print("Go from {} to {} in {} stops using line {}".format(
                        self.path[i][0], self.finish, stops +
                        self.path[j][1], self.path[i][2]
                    ))
                    i = j + 1
                    break

                # Num of stops accumulates
                stops += self.path[j][1]
