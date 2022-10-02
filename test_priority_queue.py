from graph.PriorityQueue import PriorityQueue


def test_priorityQueue():
    q = PriorityQueue()

    q.insert(3, 1)
    assert (q.removeMin() == [3, 1])

    for i in [[10, 10], [9, 1], [3, -5000]]:
        q.insert(i[0], i[1])

    assert (q.removeMin() == [3, -5000])
