# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length  = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        position_to_remove = length - n

        if position_to_remove == 0:
                return head.next
            
        current = head
        for _ in range(position_to_remove - 1):
            current =  current.next
        current.next = current.next.next

        return head

            