import unittest
from Q1 import *
from Q2 import *
from Q3 import *

import networkx as nx


class MyTestCase(unittest.TestCase):
    def test_q1(self):
        print(' -------------------------------- Q1 tests -------------------------------- ')
        self.assertEqual(safe_call(f, 10, 2, 3), 15)
        self.assertFalse(safe_call(f, 5, "abc", 3))
        self.assertEqual(safe_call(f, 5, 7.0, 3), 15.0)
        self.assertFalse(safe_call(f, "abc", 2.1, 3))
        self.assertFalse(safe_call(f, " ", " ", 3))
        print()

    def test_q2(self):
        print(' -------------------------------- Q2 tests -------------------------------- ')
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
        print()

    def test_q3(self):
        print(' -------------------------------- Q3 tests -------------------------------- ')
        list1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
        self.assertEqual(print_sorted(list1), [('a', 5), ('b', [1, 2, 3, 4]), ('c', 6)])
        self.assertNotEqual(print_sorted(list1), [('b', 5), ('b', [1, 2, 3, 4]), ('c', 6)])
        list2 = {'student1': ('bhanu', 10), 'student4': ('uma', 12),
                 'student3': ('suma', 11), 'student2': ('ravi', 11),
                 'student5': ('gayatri', 9)}
        self.assertEqual(print_sorted(list2),
                         [('student1', (10, 'bhanu')), ('student2', (11, 'ravi')), ('student3', (11, 'suma')),
                          ('student4', (12, 'uma')), ('student5', (9, 'gayatri'))])
        self.assertNotEqual(print_sorted(list2),
                            [('student2', (10, 'bhanu')), ('student2', (11, 'ravi')), ('student3', (11, 'suma')),
                             ('student4', (12, 'uma')), ('student5', (9, 'gayatri'))])
        list3 = [1, [1, 2, 3], 2, 0, 12]
        self.assertEqual(print_sorted(list3), [0, 1, 12, 2, [1, 2, 3]])
        self.assertNotEqual(print_sorted(list3), [12, 1, 12, 2, [1, 2, 3]])
        list4 = {5: 5, 'c': 6, 'b': [1, 3, 2, 4]}
        self.assertEqual(print_sorted(list4), [('b', [1, 2, 3, 4]), ('c', 6), (5, 5)])
        self.assertNotEqual(print_sorted(list4), [('b', 5), ('b', [1, 2, 3, 4]), ('c', 6)])
        set01 = {'Apples', ('Bananas', 'Oranges')}
        self.assertEqual(print_sorted(set01), {('Bananas', 'Oranges'), 'Apples'})
        self.assertNotEqual(print_sorted(set01), {})
        print()


if __name__ == '__main__':
    unittest.main()
