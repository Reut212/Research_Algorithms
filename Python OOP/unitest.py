import unittest
from Q2 import *
from Q3 import *


class MyTestCase(unittest.TestCase):
    print(' -------------------------------- Q2 tests -------------------------------- ')

    def test_q2(self):
        self.assertEqual(power(x=2), 4)
        self.assertNotEqual(power(x=2), 5)
        self.assertEqual(power(), "Please insert a valid parameters")
        self.assertNotEqual(power(), 5)
        self.assertEqual(power(2), "I already told you that the answer is 4!")
        self.assertNotEqual(power(x=2), 5)
        self.assertEqual(mul_dif(x=2.1, y=4), 8.4)
        self.assertEqual(mul_dif(x=2.1), "Please insert a valid parameters")
        self.assertNotEqual(mul_dif(x=2), 5)
        self.assertEqual(mul_dif(2.1, 4), "I already told you that the answer is 8.4!")
        self.assertEqual(sum_numbers(3, 4), 7)
        self.assertEqual(sum_numbers(2, 1), 3)
        self.assertEqual(sum_numbers(3, 4), "I already told you that the answer is 7!")
        print()

        print(' -------------------------------- Q3 tests -------------------------------- ')

    def test_q3(self):
        list1 = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]],
        ])
        self.assertEqual(list1[0, 1, 3], 66)
        self.assertEqual(list1[0], [[1, 2, 3, 33], [4, 5, 6, 66]])
        self.assertEqual(list1[4], None)
        list1[2] = 3
        self.assertEqual(list1[0], [[1, 2, 3, 33], [4, 5, 6, 66]])
        self.assertEqual(list1, [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], 3])
        self.assertEqual(list1[None], None)
        self.assertEqual(list1[1], [[7, 8, 9, 99], [10, 11, 12, 122]])
        self.assertEqual(list1, [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], 3])
        del (list1[1])
        self.assertEqual(list1, [[[1, 2, 3, 33], [4, 5, 6, 66]], 3])
        print()


if __name__ == '__main__':
    unittest.main()
