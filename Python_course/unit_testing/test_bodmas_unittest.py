import bodmas
import unittest


class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)
        self.assertEqual(bodmas.addition(9, 9), 18)
        self.assertEqual(bodmas.addition(19, 15), 34)

    def test_addition(self):
        self.assertEqual(bodmas.subtraction(3, 1), 2)
        self.assertEqual(bodmas.subtraction(9, 1), 8)



if __name__ == '__main__':
    unittest.main()