# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        curr = node
        if list1 == None and list2 == None:
            return None
        while list1 != None or list2 != None:

            val1 = 101
            val2 = 101
            if list1 != None:
                val1 = list1.val
            if list2!= None:
                val2 = list2.val
            
            if val1 < val2:
                curr.val = val1
                list1 = list1.next
            else:
                curr.val = val2
                list2 = list2.next
            if list1 != None or list2 != None:
                curr.next = ListNode()
                curr = curr.next
            
        return node

                
            


