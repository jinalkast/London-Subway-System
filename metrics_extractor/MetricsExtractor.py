from collections import defaultdict


class MetricsExtractor:
    def compute_avg_degree(graph):
        num_of_edges = sum(len(Node.connections)
                           for Node in graph.graph.values())
        return (num_of_edges / len(graph.graph))

    def compute_sum_of_degrees(graph):
        degreesCount = defaultdict(lambda: 0)

        for i in graph.graph.values():
            degreesCount[len(i.connections)] += 1

        return degreesCount

    def return_zone_list(graph):
        stationsInZone = defaultdict(set)
        for i in graph.graph:
            # Incase a zone is X.5, if it isn't repeat values
            # don't get added since datatype is a set
            stationsInZone[round(graph.graph[i].zone + .1)].add(i)
            stationsInZone[round(graph.graph[i].zone)].add(i)
        return stationsInZone
