from subway_patrol.SubwayPatrol import SubwayPatrol
from graph_builder.GraphBuilder import GraphBuilder


def test_travelling_salesman():
    pathToStations = "_dataset/london.stations.csv"
    pathToConnections = "_dataset/london.connections.csv"
    g = GraphBuilder.build(pathToStations, pathToConnections)
    assert SubwayPatrol.travellingSalesmanProblem(g, [11]) is None
    assert SubwayPatrol.travellingSalesmanProblem(
        g, [15, 32]).total_path_length == 34.0
    assert SubwayPatrol.travellingSalesmanProblem(
        g, [13, 75, 100]).total_path_length == 109.0
    assert SubwayPatrol.travellingSalesmanProblem(
        g, [16, 4, 121, 111]).total_path_length == 146.0
    assert SubwayPatrol.travellingSalesmanProblem(
        g, [14, 5, 131, 95, 86]).total_path_length == 168.0
