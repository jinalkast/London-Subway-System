from graph_builder.GraphBuilder import GraphBuilder
from metrics_extractor.MetricsExtractor import MetricsExtractor


def test_metrics_extractor():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)

    assert MetricsExtractor.compute_avg_degree(g) == 2.6887417218543046
    assert MetricsExtractor.compute_sum_of_degrees(g) == {
        5: 5, 3: 15, 4: 43, 2: 191, 10: 1, 6: 16, 1: 24, 7: 2, 8: 4, 12: 1}
