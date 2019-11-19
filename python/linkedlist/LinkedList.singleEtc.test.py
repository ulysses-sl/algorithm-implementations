import unittest
from LinkedList import SinglyLinkedList, are_equal, generate_list, reverse_list, reverse_list_rec


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_list(None), None)

    def test_single(self):
        self.assertTrue(are_equal(
            reverse_list(generate_list([1])),
            generate_list([1])
        ))

    def test_many(self):
        self.assertTrue(are_equal(
            reverse_list(generate_list([1, 2, 3, 4])),
            generate_list([4, 3, 2, 1])
        ))


class TestReverseRec(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_list_rec(None), None)

    def test_single(self):
        self.assertTrue(are_equal(
            reverse_list_rec(generate_list([1])),
            generate_list([1])
        ))

    def test_many(self):
        self.assertTrue(are_equal(
            reverse_list_rec(generate_list([1, 2, 3, 4])),
            generate_list([4, 3, 2, 1])
        ))


if __name__ == '__main__':
    unittest.main()
