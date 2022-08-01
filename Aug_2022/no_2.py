from util.Util import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #自己解法
        flag = False
        tmp = None
        res = None
        while l1 or l2 or flag:
            if not l1:
                l1 = ListNode(val=0)
            if not l2:
                l2 = ListNode(val=0)
            if flag:
                val = l1.val + l2.val + 1
            else:
                val = l1.val + l2.val
            flag, out = (True, val - 10) if val >= 10 else (False, val)
            if not tmp:
                tmp = ListNode(val=out)
                res = tmp
            else:
                tmp.next = ListNode(val=out)
                tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        return res


if __name__ == '__main__':
    l1c = ListNode(val=5)
    l1b = ListNode(val=3, next=l1c)
    l1a = ListNode(val=4,next=l1b)
    l1 = ListNode(val=2,next=l1a)

    l2b = ListNode(val=4)
    l2a = ListNode(val=6, next=l2b)
    l2 = ListNode(val=5, next=l2a)
    s = Solution()
    print(s.addTwoNumbers(l1, l2))