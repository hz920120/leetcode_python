class Solution(object):
    def reverseList(self, node):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not node:
            return node

        tmp = None
        while node:
            node.next, node, tmp = tmp, node.next, node
        return tmp