# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head1: Optional[ListNode])-> (Optional[ListNode], int):
            prev = None
            curr = head1
            count = 0
            while curr != None:
                count +=1
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return (prev, count)
        if head.next == None:
            return None
        rHead, s = reverseList(head)
        k = 1
        curr = rHead
        if n == 1:
            rHead = rHead.next
        else:
            while k <n-1 and curr != None:
                curr = curr.next
                k+=1
        
        curr.next = curr.next.next
        return reverseList(rHead)[0]
