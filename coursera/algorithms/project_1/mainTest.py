print("Project - 1")
EMPTY_SET = set([])

EX_GRAPH0 = {0: {1, 2},
             1: EMPTY_SET,
             2: EMPTY_SET}

EX_GRAPH1 = {0: {1, 5, 4},
             1: {2, 6},
             2: {3},
             3: {0},
             4: {1},
             5: {2},
             6: EMPTY_SET}

EX_GRAPH2 = {0: {1, 5, 4},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: EMPTY_SET,
             7: {3},
             8: {1, 2},
             9: {0, 4, 5, 6, 7, 3}}


def make_complete_graph(num_nodes):
    resulted_graph = dict()
    if num_nodes < 0:
        return resulted_graph

    for from_vert in range(0, num_nodes):
        for to_vert in range(0, num_nodes):
            if from_vert != to_vert:
                if from_vert not in resulted_graph.keys():
                    resulted_graph[from_vert] = set([])
                resulted_graph.get(from_vert).add(to_vert)

    return resulted_graph


complete_graph = make_complete_graph(3)
for eachVert in complete_graph.keys():
    print(str(eachVert) + " -> " + str(complete_graph.get(eachVert)))


def compute_in_degrees(digraph):
    in_degree_count = dict()
    for eachVert in digraph.keys():
        in_degree_count[eachVert] = 0

    for eachVert in digraph.keys():
        for eachAdjVert in digraph.get(eachVert):
            in_degree_count[eachAdjVert] += 1

    return in_degree_count


print("in-degree calculator")

print(compute_in_degrees(complete_graph))
print(compute_in_degrees(EX_GRAPH0))

def in_degree_distribution(digraph):

