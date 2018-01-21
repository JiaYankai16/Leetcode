# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        p=ListNode(0)
        m=p
        while(l1 or l2):
            if(l1 and l2):
                if l1.val<=l2.val:
                    p.val=l1.val
                    l1=l1.next
                else:
                    p.val=l2.val
                    l2=l2.next
            elif(l1 and l2 is None):
                p.val=l1.val
                l1=l1.next
            elif(l2 and l1 is None):
                p.val=l2.val
                l2=l2.next
            if(l1 or l2):
                p.next=ListNode(0)
                p=p.next 
        return m