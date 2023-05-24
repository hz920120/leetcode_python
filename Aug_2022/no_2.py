from util.Util import ListNode

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #
    #     #自己解法
    #     flag = False
    #     tmp = None
    #     res = None
    #     while l1 or l2 or flag:
    #         if not l1:
    #             l1 = ListNode(val=0)
    #         if not l2:
    #             l2 = ListNode(val=0)
    #         if flag:
    #             val = l1.val + l2.val + 1
    #         else:
    #             val = l1.val + l2.val
    #         flag, out = (True, val - 10) if val >= 10 else (False, val)
    #         if not tmp:
    #             tmp = ListNode(val=out)
    #             res = tmp
    #         else:
    #             tmp.next = ListNode(val=out)
    #             tmp = tmp.next
    #         l1 = l1.next
    #         l2 = l2.next
    #     return res
    def addTwoNumbers(self, l1, l2):
        def method(l1, l2):
            a = ''
            b = ''
            while l1 or l2:
                if l1:
                    a += str(l1.val)
                    l1 = l1.next
                if l2:
                    b += str(l2.val)
                    l2 = l2.next
            n = int(a[::-1]) + int(b[::-1])
            res = str(n)
            # [int(x) for x in [*res]]
            node = None
            for i in range(len(res)):
                if node:
                    tmp = ListNode(int(res[i]))
                    tmp.next = node
                    node = tmp
                else:
                    node = ListNode(int(res[i]))
            return node
        haja = method(l1, l2)
        return haja

if __name__ == '__main__':
    # l1c = ListNode(val=5)
    l1b = ListNode(val=3, )
    l1a = ListNode(val=4,next=l1b)
    l1 = ListNode(val=1,next=l1a)

    l2b = ListNode(val=4)
    l2a = ListNode(val=6, next=l2b)
    l2 = ListNode(val=5, next=l2a)
    s = Solution()
    print(s.addTwoNumbers(l1, l2))


    # def method(l1, l2):
    #     a = ''
    #     b = ''
    #     while l1 or l2:
    #         if l1:
    #             a += str(l1.val)
    #             l1 = l1.next
    #         if l2:
    #             b += str(l2.val)
    #             l2 = l2.next
    #     n = int(a) + int(b)
    #     res = str(n)
    #     print([int(x) for x in [*res]])
    # method(l1, l2)