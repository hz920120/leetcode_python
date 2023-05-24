from util.Util import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        class RetureType():
            def __init__(self, isSearch, max_value, min_value):
                self.isSearch = isSearch
                self.max_value = max_value
                self.min_value = min_value

        def isBST(root):
            rt = process(root)
            return rt.isSearch

        def process(root):
            if not root:
                rt = RetureType(True, None, None)
                return rt

            l_node = process(root.left)
            r_node = process(root.right)
            l_min = l_node.min_value if l_node.min_value else root.val
            r_max = r_node.max_value if r_node.max_value else root.val
            isValid = l_node.isSearch and r_node.isSearch and (True if not l_node.max_value else l_node.max_value <
                                                                       root.val) and (True if not r_node.min_value else r_node.min_value >
                                                                       root.val)
            rt = RetureType(isValid, r_max, l_min)
            return rt


        return isBST(root)


if __name__ == '__main__':
    s = Solution()
    l = TreeNode(1)
    r_l = TreeNode(3)
    r_r = TreeNode(6)
    r = TreeNode(4, r_l, r_r)
    root = TreeNode(5, l, r)

    print(s.isValidBST(root))