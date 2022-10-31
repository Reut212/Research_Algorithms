# graph is in adjacent list representation
import doctest
import networkx as nx



def breadth_first_search(start, end, neighbor_function):
    # initialize queue parent and visited
    # push the first path into the queue
    queue = [start]
    parent = {}
    # push the first path into visited
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
        return print('There is no path between ' + str(start) + ' and ' + str(end))


# [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
# requested_path = [(0,0), (0,1), (1,1), (2,1), (2,2)]
# [(0,0) : [(1,0), (-1,0), (0,1), (0,-1)]
# [(0,1) : [(1,1), (-1,1), (0,2), (0,0)]
# [(0,2) : [(1,2), (-1,2), (0,3), (0,1)]
# [(1,0) : [(2,0), (0,0), (1,1), (1,0)]
# [(1,1) : [(2,1), (0,1), (1,2), (1,0)]
# [(1,2) : [(2,2), (1,2), (1,3), (1,1)]
# [(2,0) : [(3,0), (1,0), (2,1), (2,-1)]
# [(2,1) : [(3,1), (1,1), (2,2), (2,0)]
# [(2,2)]


def four_neighbor_function(node: any) -> list:  # [(0,1) , (-1,0), (0,1), (0,-1)]
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def main():
    g1 = nx.Graph()
    g1.add_nodes_from(range(1, 4))
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 3)
    print(breadth_first_search(1, 5, g1.neighbors))
    # print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))


if __name__ == '__main__':
    main()
