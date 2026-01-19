# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        ---- Solution Intent (carry bits) ----
        use integer division to get carry
        use modulo to get one's
        loop while l1 or l2 not ended or carry != 0
        """
        
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2 or carry: #l1 and l2 can have different lengths, if l1 and l2 ends, we still need 1 last loop if carry == 1
            val1 = l1.val if l1 else 0 #if end of list just treat it as 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10 #update carry after sum is calculated
            nextNode = ListNode(total % 10) #ignore digits > 9
            curr.next = nextNode
            curr = curr.next
            if l1: l1 = l1.next #walk list till None (end of list)
            if l2: l2 = l2.next
        return head.next