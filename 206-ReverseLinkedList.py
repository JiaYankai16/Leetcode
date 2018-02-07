# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        taglist=[]
        while head:
            taglist.append(head.val)
            head=head.next
        p=t=ListNode(0)
        for i in range(len(taglist)-1,-1,-1):
            p.next=ListNode(0)
            p=p.next
            p.val=taglist[i]
        return t.next
            
        