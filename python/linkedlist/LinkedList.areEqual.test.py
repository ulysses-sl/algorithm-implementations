import unittest
from LinkedList import SinglyLinkedList, are_equal, generate_list


class TestAreEqual(unittest.TestCase):
    def test_both_empty(self):
        self.assertTrue(are_equal(None, None))

    def test_one_empty(self):
        self.assertFalse(are_equal(SinglyLinkedList(1), None))

    def test_unequal(self):
        lst1 = SinglyLinkedList(1)
        lst2 = SinglyLinkedList(2)
        self.assertFalse(are_equal(lst1, lst2))

    def test_equal(self):
        lst1 = SinglyLinkedList(1)
        lst2 = SinglyLinkedList(1)
        self.assertTrue(are_equal(lst1, lst2))

    def test_extend(self):
        lst1 = SinglyLinkedList(1)
        lst2 = SinglyLinkedList(1)
        lst2.next = SinglyLinkedList(2)
        self.assertFalse(are_equal(lst1, lst2))


class TestGenerateList(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(are_equal(generate_list([]), None))

    def test_one(self):
        self.assertTrue(are_equal(generate_list([1]), SinglyLinkedList(1)))

    def test_multiple(self):
        lst2 = SinglyLinkedList(1)
        lst2.next = SinglyLinkedList(2)
        self.assertTrue(are_equal(generate_list([1, 2]), lst2))


if __name__ == '__main__':
    unittest.main()
