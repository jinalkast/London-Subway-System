class Itinerary():
    def __init__(self, parent_list, start, finish):
        self.start = start
        self.finish = finish
        self.path = self.compute_path(parent_list)
        self.total_path_length = sum(i[1] for i in self.path)

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

    def combine_itineraries(i1, i2):
        i1.finish = i2.finish
        for i in i2.path:
            i1.path.append(i)
        i1.total_path_length += i2.total_path_length
        return i1

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
                        self.path[i][0], self.path[j][0],
                        stops, self.path[i][2]
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
