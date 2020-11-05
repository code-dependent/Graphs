
from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for tup in ancestors:
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])

        graph.add_edge(tup[1], tup[0])

    if len(graph.get_neighbors(starting_node)) == 0:
        return -1

    stack = Stack()
    stack.push([starting_node])
    paths =[]

    while stack.size() > 0:
        path = stack.pop()
        paths.append(path)

        for n in graph.get_neighbors(path[-1]):
            stack.push(path+[n])

    paths.sort(key=lambda path: (len(path), -path[-1]))

    return paths[-1][-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,8))