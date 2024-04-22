# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.iter = self

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iter:
            raise StopIteration
        next_node = self.iter
        self.iter = self.iter.next
        return next_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode()
        cur_node = s
        c = 0
        pre_node = None
        while l1 and l2:
            res = l1.val + l2.val + c
            c = 0
            if res >= 10:
                c = 1
                res %= 10
            cur_node.val = res
            cur_node.next = ListNode()
            pre_node = cur_node
            cur_node = cur_node.next
            l1, l2 = l1.next, l2.next

        rem_l = l1 if l1 else l2
        while rem_l:
            res = rem_l.val + c
            c = 0
            if res >= 10:
                c = 1
                res %= 10
            cur_node.val = res
            cur_node.next = ListNode()
            pre_node = cur_node
            cur_node = cur_node.next
            rem_l = rem_l.next
        if c == 1:
            cur_node.val = c
        else:
            pre_node.next = None
        return s


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution().addTwoNumbers(l1, l2)

    a1 = [str(d.val) for d in l1]
    a1.reverse()
    a2 = [str(d.val) for d in l2]
    a2.reverse()
    a = [str(d.val) for d in s]
    a.reverse()
    n1 = "".join(a1)
    n2 = "".join(a2)
    n = "".join(a)
    print(f"{n1} + {n2} = {n}")


# a1 + b1 + c1 + d1 = r1
# a2 + b2 + c2 + d2 = r2
# a3 + b3 + c3 + d3 = r3
# a4 + b4 + c4 + d4 = r4

# a1 + a2 + a3 + a4 = ca
# b1 + b2 + b3 + b4 = cb
# c1 + c2 + c3 + c4 = cc
# d1 + d2 + d3 + d4 = cd


