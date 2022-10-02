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
