# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Define a function that takes the head nodes of two linked lists (l1 and l2)
        # Create a placeholder node to act as the starting anchor for the new result list
        dummy = ListNode()
        # Create a pointer 'curr' to build the new list node by node without losing the start
        curr = dummy
        # Initialize 'carry' to 0 to store any overflow when two digits add up to 10 or more
        carry = 0

        # Keep looping as long as there are nodes left in l1, l2, or there is a leftover carry
        while l1 or l2 or carry:
            # Start the current digit's sum with whatever carried over from the previous step
            total = carry
            # Check if l1 still has a node to process
            if l1:
                # Add l1's current digit to the total
                total += l1.val
                # Advance l1's pointer to the next node
                l1 = l1.next
            # Check if l2 still has a node to process
            if l2:
                # Add l2's current digit to the total
                total += l2.val
                # Advance l2's pointer to the next node
                l2 = l2.next

            # Calculate the new carry for the next position (e.g., 15 // 10 = 1)
            carry = total // 10
            # Create a new node with the single-digit remainder (e.g., 15 % 10 = 5) and link it
            curr.next = ListNode(total % 10)
            # Move the current pointer forward to the newly created node
            curr = curr.next

        # Return the node right after the dummy node, which is the actual head of the answer list
        return dummy.next

        