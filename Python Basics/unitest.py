import unittest
from Q1 import *
from Q2 import *

import networkx as nx


class MyTestCase(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(safe_call(f, 10, 2, 3), 15)
        self.assertFalse(safe_call(f, 5, "abc", 3))
        self.assertEqual(safe_call(f, 5, 7.0, 3), 15.0)
        self.assertFalse(safe_call(f, "abc", 2.1, 3))
        self.assertFalse(safe_call(f, " ", " ", 3))

    def test_q2(self):
        g = nx.Graph()
        g.add_nodes_from(range(1, 4))
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        self.assertEqual(breadth_first_search(1, 3, g.neighbors), [1, 3])
        self.assertNotEqual(breadth_first_search(1, 3, g.neighbors), [3, 1])
        g.add_edge(3, 1)
        self.assertNotEqual(breadth_first_search(1, 3, g.neighbors), [3, 1])
        self.assertNotEqual(breadth_first_search(1, 3, g.neighbors), [10, 1])
        g.remove_edge(1, 3)
        self.assertEqual(breadth_first_search(1, 2, g.neighbors), [1, 2])
        self.assertEqual(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function),
                         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
        self.assertFalse(breadth_first_search(1, 5, g.neighbors))


if __name__ == '__main__':
    unittest.main()
