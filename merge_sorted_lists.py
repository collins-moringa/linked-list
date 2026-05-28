from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next
def to_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


sol = Solution()
print(to_list(sol.mergeTwoLists(to_linked_list([1,2,4]), to_linked_list([1,3,4]))))  # [1,1,2,3,4,4]
print(to_list(sol.mergeTwoLists(to_linked_list([]),      to_linked_list([]))))       # []
print(to_list(sol.mergeTwoLists(to_linked_list([]),      to_linked_list([0]))))      # [0]
