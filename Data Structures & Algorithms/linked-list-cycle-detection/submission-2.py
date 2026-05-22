# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        currFast = head
        currSlow = head
        while currFast.next !=None:
            currFast = currFast.next.next
            currSlow = currSlow.next
            if currFast == None:
                break
            if currFast == currSlow:
                return True
            
        
        return False
            
