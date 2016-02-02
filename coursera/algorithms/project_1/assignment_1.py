""" Solution for the first Course assignment.

"""
EX_GRAPH0 = {0: {1, 2},
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: {1, 5, 4},
             1: {2, 6},
             2: {3},
             3: {0},
             4: {1},
             5: {2},
             6: set([])}

EX_GRAPH2 = {0: {1, 5, 4},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: set([]),
             7: {3},
             8: {1, 2},
             9: {0, 4, 5, 6, 7, 3}}


def make_complete_graph(num_nodes):
    """
    :param num_nodes: Number of vertices for this graph.
    :return: Complete graph out of the given num of verts.
    """
    resulted_graph = dict()
    if num_nodes < 0:
        return resulted_graph
    if num_nodes == 1:
        resulted_graph[0] = set([])

    for from_vert in range(0, num_nodes):
        for to_vert in range(0, num_nodes):
            if from_vert != to_vert:
                if from_vert not in resulted_graph.keys():
                    resulted_graph[from_vert] = set([])
                resulted_graph.get(from_vert).add(to_vert)

    return resulted_graph


def print_graph(digraph):
    """
    :param digraph: Prints supplied directed Graph.
    :return:
    """
    for each_vert in digraph.keys():
        print(str(each_vert) + " -> " + str(digraph.get(each_vert)))

print("EX_Graph 0: ")

print_graph(EX_GRAPH0)
print("make_complete_graph with one vertex: ")
print_graph(make_complete_graph(1))


def compute_in_degrees(digraph):
    """
    :param digraph: Directed Graph.
    :return: Number of in-degrees for each vertex
    """
    in_degree_count = dict()
    for each_vert in digraph.keys():
        in_degree_count[each_vert] = 0

    for each_vert in digraph.keys():
        for each_adj_vertex in digraph.get(each_vert):
            in_degree_count[each_adj_vertex] += 1

    return in_degree_count


print("in-degree calculator")

print(compute_in_degrees(EX_GRAPH0))


def in_degree_distribution(digraph):
    """
    :param digraph: Directed Graph representation.
    :return: Dictionary of the in-degree population.
    """
    result = dict()
    in_degree_map = compute_in_degrees(digraph)
    for num_in_degrees in in_degree_map.values():
        if num_in_degrees not in result.keys():
            result[num_in_degrees] = 1
        else:
            result[num_in_degrees] += 1

    return result

print(in_degree_distribution(EX_GRAPH0))
