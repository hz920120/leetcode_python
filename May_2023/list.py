from typing import Optional

from util.Util import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        def getNum(x, n):
            return x * (10 ** n)

        flag = False
        head = None
        res = None
        while l1 or l2 or flag:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + flag
            if v >= 10:
                if head is not None:
                    head.next = ListNode(v - 10)
                    head = head.next
                else:
                    head = ListNode(v - 10)
                    res = head
                flag = True
            else:
                if head is not None:
                    head.next = ListNode(v)
                    head = head.next
                else:
                    head = ListNode(v)
                    res = head
                flag = False
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res

    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return head
    #
    #     def swap_two_nodes(n_left: ListNode, n_right: ListNode, ne: ListNode):
    #         n_right.next = n_left
    #         n_left.next = ne
    #         return ne
    #
    #     curr = head
    #     curr_next = head.next
    #     if curr_next is None:
    #         return curr
    #     else:
    #         res = curr_next
    #     while curr or curr_next:
    #         temp = curr_next.next
    #         new_head = swap_two_nodes(curr, curr_next, temp)
    #         if new_head:
    #             curr = new_head
    #             curr_next = curr.next
    #         else:
    #             break
    #     return res


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap_two_nodes(n_left: ListNode, n_right: ListNode):
            n_right.next = n_left
            return n_left

        def process(head):
            if not head:
                return head
            curr = head
            curr_next = head.next
            if curr_next is None:
                return curr
            else:
                res = curr_next
                temp = res.next
                tail = swap_two_nodes(curr, curr_next)
                tail.next = process(temp)
            return res
        return process(head)


if __name__ == '__main__':
    list4 = ListNode(val=4)
    list3 = ListNode(val=3, next=list4)
    list2 = ListNode(val=2, next=list3)
    list1 = ListNode(val=1, next=list2)
    s = Solution()
    res = s.swapPairs(list1)
    print(res.val)