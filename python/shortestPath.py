from math import radians, cos, sin, asin, sqrt
from python.graph import Itinerary
from python.PriorityQueue import PriorityQueue


class PathFactory():

    def dijkstra(graph, src, dest):
        # is updated
        nodes_visted = 0
        edges_crossed = 0
        dist = {}   # dist values used to pick minimum
        # weight edge in cut

        graph.parent = {}
        graph.parent[src] = [src, 0, 0]
        # pqueue represents set E
        pQueue = PriorityQueue()

        # Initialize pqueue with all vertices.
        # dist value of all vertices
        for id in graph.graph:
            dist[id] = 1e7
            pQueue.insert(id, 1e7)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        pQueue.changeVal(src, 0)
        dist[src] = 0

        # In the following loop,
        # pqueue contains all nodes
        # whose shortest distance is not yet finalized.
        while not pQueue.isEmpty():
            edges_crossed += 1
            # Extract the vertex
            # with minimum distance value
            newPqueueNode = pQueue.removeMin()
            u = newPqueueNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for neighbour in graph.graph[u].connections:
                nodes_visted += 1
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
                    # in pqueue also
                    pQueue.changeVal(neighbourID, dist[neighbourID])

        # print("Nodes visited {}".format(nodes_visted))
        # print("Edges crossed {}".format(edges_crossed))

        return Itinerary(graph.parent, src, dest)

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

        nodes_visted = 0
        edges_crossed = 0

        # Initialize pqueue with all vertices.
        # dist value of all vertices
        for id in graph.graph:
            gScore[id] = 1e7
            fScore[id] = 1e7
            pQueue.insert(id, 1e7)

        pQueue.changeVal(src, 0)
        gScore[src] = 0
        fScore[src] = 0

        # In the following loop,
        # pqueue contains all nodes
        # whose shortest distance is not yet finalized.
        while not pQueue.isEmpty():
            edges_crossed += 1
            pQueueNode = pQueue.removeMin()
            current = pQueueNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for neighbour in graph.graph[current].connections:
                nodes_visted += 1
                neighbourID = neighbour[0]
                line = neighbour[1]
                neighbourDist = neighbour[2]

                temp_gScore = gScore[current] + neighbourDist

                # Recalculate shortest distance
                if temp_gScore < gScore[neighbourID]:
                    gScore[neighbourID] = temp_gScore
                    fScore[neighbourID] = temp_gScore + \
                        hScore(current, neighbourID)
                    graph.parent[neighbourID] = [
                        current, neighbourDist, line]

                    if neighbourID in pQueue.queue:
                        pQueue.changeVal(neighbourID, fScore[neighbourID])

        # print("Nodes visited {}".format(nodes_visted))
        # print("Edges crossed {}".format(edges_crossed))

        return Itinerary(graph.parent, src, dest)
