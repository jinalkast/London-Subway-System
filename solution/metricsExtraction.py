from collections import defaultdict


class MetricsExtractor:
    def compute_avg_degree(graph):
        num_of_edges = sum(len(Node.connections)
                           for Node in graph.values())
        return (num_of_edges / len(graph))

    def compute_sum_of_degrees(graph):
        degreesCount = defaultdict(lambda: 0)

        for i in graph.values():
            degreesCount[len(i.connections)] += 1

        return degreesCount

    def return_zone_list(graph):
        stationsInZone = defaultdict(set)
        for i in graph:
            stationsInZone[round(graph[i].zone + .1)].add(i)
            stationsInZone[round(graph[i].zone)].add(i)
        return stationsInZone
