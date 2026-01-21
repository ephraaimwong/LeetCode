# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyHead = head
        currentNode = head
        while currentNode and currentNode.next:
            currentVal = currentNode.val
            nextVal = currentNode.next.val

            if currentVal == nextVal: #will rerun this check after killing repeated
                currentNode.next = currentNode.next.next #set .next to 2 ahead
                killNode = currentNode.next
                killNode = None #kill the repeated node
            else: # only triggers when current != next
                currentNode = currentNode.next
            
        return dummyHead