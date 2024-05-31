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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = list1
        if list1.val > list2.val:
            head = list2

        while list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1

            if not list1.next:
                list1.next = list2
                break
            else:
                if list2.val < list1.next.val:
                    list1.next, list1 = list2, list1.next
                else:
                    list1 = list1.next

        return head


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5)))
    sol = Solution()
    print(sol.mergeTwoLists(list1, list2))
