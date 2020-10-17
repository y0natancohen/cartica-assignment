from pygraph.classes.graph import graph as Graph
from pygraph.algorithms.searching import breadth_first_search as bfs
import json


def _get_list_from_file(file_name, file_format):
    with open(file_name, mode='r') as f:
        if file_format == 'json':
            obj = json.load(f)
        else:
            raise NotImplementedError('format not supported')

    _validate_input(obj)
    return obj


def _validate_input(obj):
    if not isinstance(obj, list):
        raise ValueError('must be a list')
    if any([not isinstance(x, int) for x in obj]):
        raise ValueError('every element must be an integer')
    if any([x < 0 for x in obj]):
        raise ValueError('every element must be >= 0')


def _generate_graph(int_list):
    g = Graph()
    max_index = len(int_list) - 1
    g.add_nodes(list(range(len(int_list))))

    for i, x in enumerate(int_list):
        if i + x <= max_index:
            g.add_edge((i, i + x))
        if i - x >= 0 and not g.has_edge((i, i - x)):
            g.add_edge((i, i - x))

    return g


def _find_path(graph):
    return bfs(graph=graph, root=0)


def is_end_reachable(file_name, file_format):
    int_list = _get_list_from_file(file_name, file_format)
    graph = _generate_graph(int_list)                       # O(n)
    spanning_tree, order = _find_path(graph)                # O(V+E) = O(V+2V) = O(V) = O(n)
    reachable = spanning_tree.get(len(int_list) - 1) is not None
    return reachable
