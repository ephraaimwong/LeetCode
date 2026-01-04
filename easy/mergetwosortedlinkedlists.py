# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        --- Solution Intent (Zipper) ---
        we know that the 2 lists are sorted.
        we can walk the 2 lists and compare their current node values until 1 of the lists is at end.
        append that current node of non-end list to the new linked list.  
        """
        mergedHead = ListNode()
        current = mergedHead #reference the same memory block, data can and will diverge

        
        while list1 and list2: #if current node for both lists exists
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next #walk to next node, Node becomes None/null when triggered from last node and breaks the while loop
            else:
                current.next = list1
                list1 = list1.next

            current = current.next
        current.next = list1 if list1 else list2 #link to the non-ending list
        return mergedHead.next #link to the first actual sorted node
            