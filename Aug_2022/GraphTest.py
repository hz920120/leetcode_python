from util.Util import *


class Solution(object):
    def bfs(self, node):
        queue = [node]
        visited = set()
        visited.add(node)
        while queue:
            curr = queue.pop(0)
            print(curr.val)
            for no in curr.nexts:
                if no not in visited:
                    queue.append(no)

