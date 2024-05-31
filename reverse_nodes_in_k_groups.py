# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + (' -> ' + str(self.next) if self.next else '')

from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next

        n = len(arr)
        if n < k:
            return head

        for r in range(k - 1, n, k):
            l = r - k + 1
            _r = r
            for i in range(k // 2):
                arr[l], arr[_r] = arr[_r], arr[l]
                l += 1
                _r -= 1

        head = arr[0]
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
        arr[-1].next = None

        return head


if __name__ == '__main__':
    # head = [1, 9, 7, 0, 1, 8, 2, 0, 8]
    head = ListNode(1,
                    ListNode(9,
                             ListNode(7,
                                      ListNode(0,
                                               ListNode(1,
                                                        ListNode(8,
                                                                 ListNode(2,
                                                                          ListNode(0,
                                                                                   ListNode(8)))))))))
    k = 8
    sol = Solution()
    print(head)
    print(sol.reverseKGroup(head, k))