import unittest
from StackQueue import SLStack, DLQueue, SQueue, QStack1, QStack2


class SLStackTest(unittest.TestCase):
    def test_all(self):
        stack = SLStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.total(), 2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.total(), 0)


class QStack1Test(unittest.TestCase):
    def test_all(self):
        stack = QStack1()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.total(), 2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.total(), 0)


class QStack2Test(unittest.TestCase):
    def test_all(self):
        stack = QStack2()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.total(), 2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.total(), 0)


class DLQueueTest(unittest.TestCase):
    def test_all(self):
        queue = DLQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.total(), 2)
        queue.push(3)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.total(), 0)


class SQueueTest(unittest.TestCase):
    def test_all(self):
        queue = SQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.total(), 2)
        queue.push(3)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.total(), 0)


if __name__ == '__main__':
    unittest.main()
