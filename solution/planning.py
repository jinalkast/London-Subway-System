from audioop import cross
from collections import defaultdict
from solution.metricsExtraction import MetricsExtractor

class connectedComponents:

    # Returns a map where stationsInZone[i] returns a list
    # of all vertices in that zone

    def DFSUtil(graph, temp, v, visited, zone, verticesInZone):

        # Mark the starting vertex as visited and add it to stack
        visited[v] = True
        stack = [v]

        # While stack is not empty, pop vertex, mark it, and append
        # its neigbours to the stack
        while (len(stack) != 0):
            vertex = stack.pop()
            temp.append(vertex)
            for i in graph[vertex].connections:
                # Check if neighbour is in the appropriate zone
                if (i[0] in verticesInZone[zone]) and (visited[i[0]] == False):
                    visited[i[0]] = True
                    stack.append(i[0])
                    temp.append(i[0])
        return temp

    def returnCC(graph, verticesInZone):
        conectedComponentsAtZone = {}
        # Find components for every zone
        for zone in verticesInZone:
            # Initialize visited and components
            visited = {}
            components = []

            # Set all vertices In the zone to unvisited
            for i in verticesInZone[zone]:
                visited[i] = False

            # If the vertex is not visited, find its
            # component
            for v in verticesInZone[zone]:
                if not visited[v]:
                    components.append(
                        connectedComponents.DFSUtil(
                            graph, [], v, visited, zone, verticesInZone))
            conectedComponentsAtZone[zone] = components

        return conectedComponentsAtZone

    def generateCrossingEdges(graph):
        crossingEdgesInZone = defaultdict(list)
        zone_list = MetricsExtractor.return_zone_list(graph)
        for zone in zone_list:
            for node in zone_list[zone]:
                for neighbour in graph[node].connections:

                    # check if station is in two zones
                    firstZone = round(graph[neighbour[0]].zone)
                    secondZone = round(graph[neighbour[0]].zone + .1)

                    # Station is in both zones
                    if firstZone != secondZone:
                        if zone != firstZone:
                            crossingEdgesInZone[zone].append([node,neighbour[0],firstZone])
                        
                        if zone != secondZone:
                            crossingEdgesInZone[zone].append([node,neighbour[0],secondZone])
                    
                    # station only in one zone
                    else:
                        if zone != firstZone:
                            crossingEdgesInZone[zone].append([node,neighbour[0],firstZone])
                            
        return crossingEdgesInZone
        


    def printCC(cc):
        for zone in cc:
            print("Zone {} has components(s):".format(zone))
            for island in cc[zone]:
                print(" " + str(island))
            print()
