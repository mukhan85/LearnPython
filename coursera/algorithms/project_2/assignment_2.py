from collections import deque

print("Project - 2")


def bfs_visited(ugraph, start_node):
    """
    :param ugraph: Undirected graph
    :param start_node: starting point of the BFS.
    :return: nothing.
    """
    visited = {}

    for each_key in ugraph.keys():
        visited[each_key] = False

    print(visited)
    queue = deque([start_node])
    visited[start_node] = True
    visit_order = {start_node}

    while True:
        try:
            next_vert = queue.pop()
            if next_vert in ugraph.keys():
                for each_neighbour in ugraph.get(next_vert):
                    if not visited[each_neighbour]:
                        visited[each_neighbour] = True
                        queue.append(each_neighbour)
                        visit_order.add(each_neighbour)
        except IndexError:
            break
    return visit_order


graph = {"dog": {"cat"},
         "cat": {"dog"},
         "monkey": {"banana"},
         "banana": {"monkey", "ape"},
         "ape": {"banana"}}


def print_graph(digraph):
    """
    :param digraph: Prints supplied directed Graph.
    :return:
    """
    for each_vert in digraph.keys():
        print(str(each_vert) + " -> " + str(digraph.get(each_vert)))

print_graph(graph)

print(bfs_visited(graph, 4))

# def cc_visited(ugraph):
