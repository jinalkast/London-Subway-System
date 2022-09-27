import time

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
    print("A* time: " + (a_star_end - a_star_start))
    print("Djikstra time: " + (djikstra_end - djikstra_start))
    # print(compute_avg_degree(g))

main()