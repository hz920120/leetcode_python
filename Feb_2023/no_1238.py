# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.Util import ListNode

class Solution:
    def reverseList(self, head: ListNode):
        if not head:
            return head

        ne = None
        while head:
            tmp = head.next
            head.next = ne
            ne = head
            head = tmp

        return ne