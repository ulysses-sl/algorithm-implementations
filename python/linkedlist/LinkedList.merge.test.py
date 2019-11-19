import unittest
from LinkedList import SinglyLinkedList, generate_list, merge_lists, merge_k_lists, are_equal, add_little_endian, add_big_endian


def generateTestList1():
    return generate_list([1, 3, 3, 4, 6])


def generateTestList2():
    return generate_list([1, 2, 5, 6, 7])


def generateTestList3():
    return generate_list([1, 1, 2, 3, 3, 4, 5, 6, 6, 7])


def generateTestList4():
    return generate_list([1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7])


class TestMergeLists(unittest.TestCase):
    def test_both_empty(self):
        lst = merge_lists(None, None)
        self.assertTrue(are_equal(lst, None))

    def test_one_empty(self):
        lst = merge_lists(generateTestList1(), None)
        self.assertTrue(are_equal(lst, generateTestList1()))

    def test_merge(self):
        lst = merge_lists(generateTestList1(), generateTestList2())
        self.assertTrue(are_equal(lst, generateTestList3()))


class TestMergeKLists(unittest.TestCase):
    def test_all_empty(self):
        lst = merge_k_lists([None, None, None])
        self.assertTrue(are_equal(lst, None))

    def test_one_empty(self):
        lst = merge_k_lists([generateTestList1(), None])
        self.assertTrue(are_equal(lst, generateTestList1()))

    def test_merge_three(self):
        lst = merge_k_lists([generateTestList1(), generateTestList2(), generateTestList2()])
        self.assertTrue(are_equal(lst, generateTestList4()))


class TestAddLittleEndian(unittest.TestCase):
    def test_same_len(self):
        lst1 = generate_list([2, 3, 6])
        lst2 = generate_list([5, 8, 4])
        self.assertTrue(are_equal(
            add_little_endian(lst1, lst2),
            generate_list([7, 1, 1, 1])
        ))

    def test_diff_len(self):
        lst1 = generate_list([2, 3, 6, 1, 3])
        lst2 = generate_list([5, 8, 4])
        self.assertTrue(are_equal(
            add_little_endian(lst1, lst2),
            generate_list([7, 1, 1, 2, 3])
        ))


class TestAddBigEndian(unittest.TestCase):
    def test_same_len(self):
        lst1 = generate_list([6, 3, 2])
        lst2 = generate_list([4, 8, 5])
        self.assertTrue(are_equal(
            add_big_endian(lst1, lst2),
            generate_list([1, 1, 1, 7])
        ))

    def test_diff_len(self):
        lst1 = generate_list([3, 1, 6, 3, 2])
        lst2 = generate_list([4, 8, 5])
        self.assertTrue(are_equal(
            add_big_endian(lst1, lst2),
            generate_list([3, 2, 1, 1, 7])
        ))


if __name__ == '__main__':
    unittest.main()
