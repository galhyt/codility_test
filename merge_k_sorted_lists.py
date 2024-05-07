# Definition for singly-linked list.
from typing import List, Optional


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
    def merge_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        prev, after = list1, list2
        if prev.val > after.val:
            prev, after = after, prev

        if not prev.next and not after.next:
            merged_list = after
        elif not prev.next:
            merged_list = after
        elif not after.next:
            merged_list = self.merge_lists(prev.next, after)
        else:
            merged_list = self.merge_lists(prev.next, after)

        prev.next = merged_list
        return prev

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if all(map(lambda l: not l, lists)):
            return None
        lists = [l for l in lists if l]
        if len(lists) == 1:
            return lists[0]
        merged_list = lists[0]
        for list2 in lists[1:]:
            merged_list = self.merge_lists(merged_list, list2)

        return merged_list


if __name__ == '__main__':
    arr = [
        ListNode(1, ListNode(4, ListNode(5))),  # 1->4->5,
        ListNode(1, ListNode(3, ListNode(4))),  # 1->3->4,
        ListNode(2, ListNode(6))                # 2->6
    ]

    # arr = [
    #     ListNode(1, ListNode(4)),
    #     ListNode(2,ListNode(3))
    # ]

    arr = [
        [],
        ListNode(1)
    ]

    sol = Solution()
    merged_list = sol.mergeKLists(arr)
    print(merged_list)