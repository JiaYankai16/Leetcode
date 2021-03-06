# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        taglist=[]
        while head:
            taglist.append(head.val)
            head=head.next
        return taglist==taglist[::-1]