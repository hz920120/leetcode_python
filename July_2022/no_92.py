from util.Util import ListNode


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        """
        初始化：  1. temp1 -> p1前一位
                2. temp2 -> p2后一位
                3. head -> 原始head
        代码：1. 翻转 p1~p2，记下头尾位置pre, p2
            2. temp1.next = pre
            3. p2.next = temp2
        边界条件： 如果从翻转中有头节点，则只需要把尾巴接上，返回新的头节点pre
        """
        if not head or right == 1:
            return head
        rev_head = False if left != 1 else True
        left_move = left - 1
        right_move = right - 1
        temp1, temp2, p1, p2 = head, head, head, head
        while right_move > 0 or left_move > 0:
            if left_move > 0:
                temp1 = p1
                p1 = p1.next
            p2 = p2.next
            temp2 = p2.next
            left_move -= 1
            right_move -= 1

        p2.next = None
        #
        curr, pre, p2 = p1, None, p1
        while curr:
            curr.next, curr, pre = pre, curr.next, curr
        if rev_head:
            p2.next = temp2
            return pre
        temp1.next = pre
        p2.next = temp2
        return head


if __name__ == '__main__':

    # list4 = ListNode(val=5)
    # list3 = ListNode(val=4, next=list4)
    # list2 = ListNode(val=3, next=list3)
    list1 = ListNode(val=5)
    head = ListNode(val=3, next=list1)

    s = Solution()
    print(s.reverseBetween(head, 1, 2))