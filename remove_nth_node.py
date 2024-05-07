# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ret = f"{self.val}"
        if self.next:
            ret += " -> "
            ret += self.next.__str__()
        return ret


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            if n == 1:
                return None
            return head

        arr = []
        node = head
        prev = None
        while node:
            arr.append((node, prev))
            prev = node
            node = node.next

        if len(arr) >= n:
            node, prev = arr[-n]
            if prev:
                prev.next = node.next
            else:
                head = node.next

        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    sol = Solution()
    print(sol.removeNthFromEnd(head, 2))
