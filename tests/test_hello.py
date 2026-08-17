import unittest

from hello import add, message


class TestHello(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_message(self):
        self.assertEqual(message(), "Hello from Jenkins CI!")


if __name__ == "__main__":
    unittest.main()
