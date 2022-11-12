import unittest
from Q2 import *


class MyTestCase(unittest.TestCase):
    def test_q2(self):
        print(' -------------------------------- Q2 tests -------------------------------- ')
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
    #
    # def test_q3(self):
    #
    #     print()


if __name__ == '__main__':
    unittest.main()
