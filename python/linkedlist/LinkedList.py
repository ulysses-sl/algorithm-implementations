from typing import Optional


class SinglyLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def are_equal(lst1: SinglyLinkedList, lst2: SinglyLinkedList) -> bool:
    if lst1 == lst2:
        return True
    if not lst1 or not lst2:
        return False
    while lst1 and lst2:
        if lst1.value != lst2.value:
            return False
        lst1 = lst1.next
        lst2 = lst2.next
    if lst1 == lst2:
        return True
    return False


def generate_list(arr):
    if not arr:
        return None
    head = SinglyLinkedList(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = SinglyLinkedList(arr[i])
        curr = curr.next
    return head


def is_circular(lst: SinglyLinkedList) -> bool:
    if not lst:
        return False
    slow = lst
    fast = lst
    while not slow.next or not fast.next or not fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def add_little_endian(num1: SinglyLinkedList, num2: SinglyLinkedList) -> SinglyLinkedList:
    head = SinglyLinkedList(None)
    curr = head
    carry = 0
    while num1 or num2:
        a = 0 if not num1 else num1.value
        b = 0 if not num2 else num2.value
        s = a + b + carry
        curr.next = SinglyLinkedList(s % 10)
        carry = s // 10
        curr = curr.next
        if num1:
            num1 = num1.next
        if num2:
            num2 = num2.next
    if carry == 1:
        curr.next = SinglyLinkedList(1)
    return head.next



def add_big_endian(num1: SinglyLinkedList, num2: SinglyLinkedList) -> SinglyLinkedList:
    stack1 = []
    stack2 = []
    curr = num1
    while curr:
        stack1.append(curr)
        curr = curr.next
    curr = num2
    while curr:
        stack2.append(curr)
        curr = curr.next
    head = None
    carry = 0
    while stack1 or stack2:
        a = 0 if not stack1 else stack1.pop().value
        b = 0 if not stack2 else stack2.pop().value
        s = a + b + carry
        x = SinglyLinkedList(s % 10)
        x.next = head
        head = x
        carry = s // 10
    if carry == 1:
        x = SinglyLinkedList(1)
        x.next = head
        head = x
    return head


def merge_lists(lst1: SinglyLinkedList, lst2: SinglyLinkedList) -> Optional[SinglyLinkedList]:
    if not lst1 and not lst2:
        return None
    head = SinglyLinkedList(None)
    curr = head
    while lst1 and lst2:
        if lst1.value <= lst2.value:
            curr.next = lst1
            lst1 = lst1.next
            curr = curr.next
        else:
            curr.next = lst2
            lst2 = lst2.next
            curr = curr.next
    if lst1:
        curr.next = lst1
    else:
        curr.next = lst2
    return head.next


def merge_k_lists(lsts) -> Optional[SinglyLinkedList]:
    if not lsts:
        return None
    return merge_recurse(lsts, 0, len(lsts)-1)


def merge_recurse(lsts, start, end) -> Optional[SinglyLinkedList]:
    if start > end:
        return None
    if start == end:
        return lsts[start]
    mid = (end - start) // 2 + start
    left = merge_recurse(lsts, start, mid)
    right = merge_recurse(lsts, mid+1, end)
    return merge_lists(left, right)


def reverse_list(lst: SinglyLinkedList) -> Optional[SinglyLinkedList]:
    head = None
    while lst:
        temp = lst.next
        lst.next = head
        head = lst
        lst = temp
    return head


def reverse_list_rec(lst: SinglyLinkedList) -> Optional[SinglyLinkedList]:
    def rev_rec_helper(ll):
        if not ll:
            return None, None
        head, tail = rev_rec_helper(ll.next)
        if not head:
            return ll, ll
        else:
            tail.next = ll
            ll.next = None
            return head, ll
    head, _ = rev_rec_helper(lst)
    return head


class DoublyLinkedList:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
