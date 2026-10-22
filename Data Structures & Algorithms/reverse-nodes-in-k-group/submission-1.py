# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count nodes to check if we have at least k
        curr = head 
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        # Base case: fewer than k nodes, return as-is
        if count < k:
            return head

        # Reverse first k nodes
        prev = None
        curr = head
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # head is now the tail, connect to recursively processed rest
        head.next = self.reverseKGroup(curr, k)

        # prev is the new head of the reversed group
        return prev