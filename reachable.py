from pygraph.classes.digraph import digraph as DirectedGraph
from pygraph.algorithms.searching import breadth_first_search as bfs

from input import get_list_from_file, InvalidInputError


def _validate_input(obj):
    if not isinstance(obj, list):
        raise InvalidInputError('input must be a list / array')

    if any([not isinstance(x, int) for x in obj]):
        raise InvalidInputError('every element must be an integer')

    if any([x < 0 for x in obj]):
        raise InvalidInputError('every element must be non-negative')


def _generate_directed_graph(int_list):
    g = DirectedGraph()
    max_index = len(int_list) - 1
    g.add_nodes(list(range(len(int_list))))

    for i, x in enumerate(int_list):
        if i + x <= max_index:
            g.add_edge((i, i + x))
        if i - x >= 0:
            g.add_edge((i, i - x))

    return g


def _find_path(graph):
    return bfs(graph=graph, root=0)


def is_end_reachable(int_list):
    _validate_input(int_list)
    graph = _generate_directed_graph(int_list)    # O(n)
    spanning_tree, order = _find_path(graph)      # O(V+E) = O(V+2V) = O(V) = O(n)
    max_index = len(int_list) - 1

    print('list: {}, target is {}, spanning tree from the first element: {}'.format(
        int_list, max_index, list(spanning_tree.keys())))
    reachable = spanning_tree.get(max_index) is not None
    return reachable


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("--format", help="json/csv/tsv file formats are supported")
    args = parser.parse_args()

    try:
        input_int_list = get_list_from_file(args.file_name, file_format=args.format)
        reachable = is_end_reachable(input_int_list)
        print("Last element is {}reachable from the first element".format('' if reachable else 'not '))
    except InvalidInputError as e:
        print('Error: file {} has invalid input: {}'.format(args.file_name, e))
