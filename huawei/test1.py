from util.Util import TreeNode
'''
一个有 n 户人家的村庄，有 m 条路相互连接着。村里现在要修路，每条路都有一个成本价格，
现在请你帮忙计算下，最少需要花费多少钱，就能让这 n 户人家连接起来。

cost 为一个二维数组，每个元素是一个长度为 3 的一维数组 aa ，
 a[0] 和 a[1] 表示村庄 a[0]和村庄 a[1]有一条路，修这条路的成本价格为 a[2] .

每户之间可能有多条道路连接，但不可能自己与自己相连
'''
from queue import PriorityQueue
class Solution(object):
    def miniSpanningTree(self, n, m, cost):
        def create_graph(n, m, cost):
            res = Graph()
            # n : 0~n-1
            for i in range(n):
                node = Node(i+1)
                res.nodes.append(node)
            # m
            q = PriorityQueue()
            nodes = res.nodes
            for it in cost:
                # a[0] 和 a[1] 表示村庄 a[0]和村庄 a[1]有一条路，修这条路的成本价格为 a[2]
                start, end, weight = it[0], it[1], it[2]
                start -= 1
                end -= 1
                edge1 = Edge(weight, start, end)
                edge2 = Edge(weight, end, start)
                res.edges.append(edge1)
                res.edges.append(edge2)
                nodes[start].nexts.append(nodes[end])
                nodes[start].edges.append(edge1)
                nodes[end].nexts.append(nodes[start])
                nodes[end].edges.append(edge2)
                q.put((weight, (nodes[start], nodes[end])))
                # q.put((weight, (nodes[end], nodes[start])))
            return res, q


        graph, q = create_graph(n, m, cost)
        activate_list = graph.nodes
        already = set()
        already.add(activate_list[0])
        cost = 0
        while len(already) != len(activate_list):
            temp = PriorityQueue()
            while not q.empty():
                it = q.get()
                weight, (node1, node2) = it[0], it[1]
                if node1 in already and node2 in already:
                    pass
                    # temp.put(it[0], it[1])
                    # cost += weight
                    # already.add(node2)
                    # already.add(node1)
                elif node1 in already or node2 in already:
                    cost += weight
                    already.add(node2)
                    already.add(node1)
                    while not temp.empty():
                        x = temp.get()
                        q.put(x)
                else:
                    temp.put((it[0], it[1]))
            # q = temp
        return cost


class Node:
    def __init__(self, val):
        self.val = val
        self.i = 0
        self.o = 0
        self.nexts = []
        self.edges = []

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

class Edge:
    def __init__(self, weight, fr, to):
        # int
        self.weight = weight
        # Node
        self.fr = fr
        self.fr = to

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []


if __name__ == '__main__':
    # from queue import PriorityQueue
    # q = PriorityQueue()
    # a1 = (3, ('jason',1))
    # a2 = (12, ('tyler',2))
    # a3 = (1, ('chris',3))
    # q.put(a1)
    # q.put(a2)
    # q.put(a3)
    # while not q.empty():
    #     it = q.get()
    #     print(it)
    #     a,(b,c) = it[0], it[1]
    #     print(a)
    #     print(b)
    #     print(c)
    s = Solution()
    cost = s.miniSpanningTree(6, 10,
                              [[5, 3, 8], [1, 3, 6], [2, 5, 4], [2, 3, 5], [4, 5, 6], [3, 4, 3], [2, 4, 8], [1, 2, 2],
                               [1, 4, 5], [5,6,2]])
    print(cost)
