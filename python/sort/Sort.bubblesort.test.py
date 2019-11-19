import unittest
import Sort

arr_empty = []
arr_singleton = [1]
arr_two_ordered = [1, 2]
arr_two_unordered = [2, 1]
arr_three_ordered = [1, 2, 3]
arr_three_reversed = [3, 2, 1]
arr_three_repeat = [3, 3, 3]
arr_five_ordered = [1, 2, 2, 3, 5]
arr_five_unordered = [3, 2, 5, 1, 2]


class TestBubbleSort(unittest.TestCase):
    def test_empty(self):
        on_test = arr_empty[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_empty))

    def test_single(self):
        on_test = arr_singleton[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_singleton))
        for new, old in zip(on_test, arr_singleton):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_singleton)
            )

    def test_two(self):
        on_test = arr_two_unordered[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_two_ordered))
        for new, old in zip(on_test, arr_two_ordered):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_two_ordered)
            )

    def test_three_ordered(self):
        on_test = arr_three_ordered[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_three_ordered))
        for new, old in zip(on_test, arr_three_ordered):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_three_ordered)
            )

    def test_three_reversed(self):
        on_test = arr_three_reversed[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_three_ordered))
        for new, old in zip(on_test, arr_three_ordered):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_three_ordered)
            )

    def test_three_repeat(self):
        on_test = arr_three_repeat[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_three_repeat))
        for new, old in zip(on_test, arr_three_repeat):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_three_repeat)
            )

    def test_five_ordered(self):
        on_test = arr_five_ordered[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_five_ordered))
        for new, old in zip(on_test, arr_five_ordered):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_five_ordered)
            )

    def test_five_unordered(self):
        on_test = arr_five_unordered[:]
        Sort.bubble_sort(on_test)
        self.assertEqual(len(on_test), len(arr_five_ordered))
        for new, old in zip(on_test, arr_five_ordered):
            self.assertEqual(
                new,
                old,
                "{} is not equal to {}".format(on_test, arr_five_ordered)
            )


if __name__ == '__main__':
    unittest.main()
