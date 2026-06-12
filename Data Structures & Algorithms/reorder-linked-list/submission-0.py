# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(root:ListNode) -> ListNode:
            curr = root
            prev = None
            while curr != None:
                newNode = ListNode()
                newNode.val = curr.val
                nextNode = curr.next
                newNode.next = prev
                prev = newNode
                curr = nextNode
                
            
            return prev
        leng = 0
        tmp = head
        while tmp!=None:
            tmp = tmp.next
            leng +=1
        print(leng)
        rCurr = reverseList(head)
        curr = head
        i = 0
        while i < ((leng-1)//2):
            saveNext = curr.next
            rNext = rCurr.next

            curr.next = rCurr
            rCurr.next = saveNext

            rCurr = rNext
            curr = saveNext
            i +=1
        
        if leng % 2 == 0:
            curr.next.next = None
        else:
            curr.next = None

        





                






    