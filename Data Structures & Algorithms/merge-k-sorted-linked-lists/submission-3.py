# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        pq = []

        for i in range(len(lists)):
                if lists[i] != None:
                    heapq.heappush(pq, (lists[i].val, i))
        if len(pq) == 0:
            return None
        firstElement, idxToAdd = heapq.heappop(pq)
        head = ListNode(firstElement)
        curr = head
        if lists[idxToAdd].next != None:
            lists[idxToAdd] = lists[idxToAdd].next
            heapq.heappush(pq, (lists[idxToAdd].val, idxToAdd))
        hasNext = True
        while len(pq) >0:
            
            currVal, idxToAdd = heapq.heappop(pq)
            nextNode = ListNode(currVal)
            curr.next = nextNode
            curr = curr.next
            if lists[idxToAdd].next != None:
                lists[idxToAdd] = lists[idxToAdd].next
                heapq.heappush(pq, (lists[idxToAdd].val, idxToAdd))
            


        

        return head

                
        
