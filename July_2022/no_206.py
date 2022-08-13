# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.Util import ListNode
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        curr, pre = head, None
        while curr:
            # temp = curr.next
            # curr.next = pre
            # pre = curr
            # curr = temp
            curr, curr.next, pre = curr.next, pre, curr
        return pre


if __name__ == '__main__':

    list4 = ListNode(val=5)
    list3 = ListNode(val=4, next=list4)
    list2 = ListNode(val=3, next=list3)
    list1 = ListNode(val=2, next=list2)
    head = ListNode(val=1, next=list1)

    s = Solution()
    print(s.reverseList(head))



