# Node class used by graph
class Node():
    def __init__(self, lat, long, name, zone) -> None:
        self.lat = lat
        self.long = long
        self.name = name
        self.connections = []
        self.zone = zone
