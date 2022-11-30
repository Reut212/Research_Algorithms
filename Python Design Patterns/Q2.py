import doctest
from typing import Callable

import networkx as nx


def shortest_path(algorithm: Callable, out_type: str, input_data):
    """
        Receive algorithm [BFS/DFS] , shortest path/length and sorce vertex, dest vertex and the graph itself.
        There is an implementation for a shortest_path.
        Used  the same BFS Algorithm as in EX1
        >>> g1 = nx.Graph()
        >>> g1.add_nodes_from(range(0, 5))
        >>> g1.add_edge(0, 1)
        >>> g1.add_edge(0, 3)
        >>> g1.add_edge(1, 3)
        >>> g1.add_edge(2, 4)
        >>> g1.add_edge(3, 2)
        >>> print(shortest_path(dfs, "length", (0, 2, g1)))
        The length is: 3
        >>> print(shortest_path(dfs, "path", (0, 2, g1)))
        The path is: [0, 3, 2]
        >>> print(shortest_path(breadth_first_search, "length", (0, 2, g1)))
        The length is: 3
        >>> print(shortest_path(breadth_first_search, "path", (0, 2, g1)))
        The path is: [0, 3, 2]
        >>> print(shortest_path(dfs, "path", (0, 5, g1)))
        There is no path between 0 and 5
        The path is: []
    """
    graph = input_data[2]
    if isinstance(input_data, list) or isinstance(input_data, tuple):
        src = int(input_data[0])
        dst = int(input_data[1])
    else:
        raise Exception("Invalid Input")

    if out_type == "length":
        return "The length is: " + str(len(algorithm(src, dst, graph.neighbors)))
    elif out_type == "path":
        return "The path is: " + str(algorithm(src, dst, graph.neighbors))
    else:
        raise Exception("Invalid Input")


def print_path(parent, start, end):
    # push the last vertex into the requested_path
    requested_path = [end]
    # keep adding vertices until reaching to first vertex
    while parent[end] != start:
        requested_path.append(parent[end])
        end = parent[end]
    # push the first vertex into the requested_path
    requested_path.append(start)
    # reverse requested_path and print
    # print(str(reverse(requested_path)))
    return requested_path[::-1]


# reverse requested_path
def reverse(requested_path):
    new_lst = requested_path[::-1]
    return new_lst


def breadth_first_search(start, end, neighbor_function):
    # initialize queue parent and visited
    # push the first vertex into the queue
    queue = [start]
    parent = {}
    # push the first vertex into visited
    visited = [start]

    while queue:
        # get the first node from the queue
        node = queue.pop(0)  # (0,0)

        # path found
        if visited[len(visited) - 1] == end:  # (0,0) != (2,2)
            return print_path(parent, start, end)

        # going over all adjacent vertices and add each one to his parent, to the queue and mark as visited
        for adjacent in neighbor_function(node):  # [(0,1) , (-1,0), (0,1), (0,-1)]
            # found the last vertex
            if adjacent == end:
                parent[adjacent] = node
                queue.append(adjacent)
                visited.append(adjacent)
                break
            # keep looking for the last requested vertex
            if adjacent not in visited:  # (0,0) not in q
                visited.append(adjacent)
                parent[adjacent] = node
                queue.append(adjacent)
    # no path available error
    if end not in parent.keys():
        print('There is no path between ' + str(start) + ' and ' + str(end))
        return []


def dfs(start, end, neighbor_function):
    visited = []
    stack = []
    path = []

    visited.append(start)
    stack.append(start)

    while stack:
        # get the first node from the queue
        node = stack.pop()
        path.append(node)
        # going over all adjacent vertices and add each one to his parent, to the queue and mark as visited
        for adjacent in neighbor_function(node):
            if adjacent not in visited:
                visited.append(adjacent)
                stack.append(adjacent)
                if adjacent == end:
                    path.append(end)
                    return path
    # no path available error
    if end not in path:
        print('There is no path between ' + str(start) + ' and ' + str(end))
        return []


if __name__ == '__main__':
    print(doctest.testmod())
    # g1 = nx.Graph()
    # g1.add_nodes_from(range(0, 5))
    # g1.add_edge(0, 1)
    # g1.add_edge(0, 3)
    # g1.add_edge(1, 3)
    # g1.add_edge(2, 4)
    # g1.add_edge(3, 2)
    # print(shortest_path(dfs, "path", (0, 5, g1)))
    # print(shortest_path(dfs, "path", (0, 2, g1)))
