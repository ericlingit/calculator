import unittest
from calculator import add

class TestAddFunc(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_add(self):
        print(add.add(1,2,3))
        self.assertEqual(add.add(1,2,3), 6)


if __name__ == "__main__":
    unittest.main()
