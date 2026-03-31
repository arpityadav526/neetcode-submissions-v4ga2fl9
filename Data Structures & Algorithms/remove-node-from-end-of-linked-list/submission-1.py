# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.head=head
        dummy = ListNode(0, head)
        first=head
        second=dummy

        for _ in range(n):
            first=first.next

        while first:
            second=second.next
            first=first.next

        second.next=second.next.next

        return dummy.next





