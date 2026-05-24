# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currNode = ListNode()
        head = currNode
        while l1 != None or l2 != None or carry != 0:
            num1 = 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            num2 = 0
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            currSum = num1+num2+carry
            
            currDigit = currSum %10
            print(currDigit)
            carry = int(currSum / 10)
            currNode.val = currDigit
            if l1 != None or l2 != None or carry != 0:
                currNode.next = ListNode()
                currNode = currNode.next
            
        
            print("here")
        
        return head
