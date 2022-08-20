
'''
一个有 n 户人家的村庄，有 m 条路相互连接着。村里现在要修路，每条路都有一个成本价格，现在请你帮忙计算下，最少需要花费多少钱，就能让这 n 户人家连接起来。

cost 为一个二维数组，每个元素是一个长度为 3 的一维数组 aa ， a[0] 和 a[1] 表示村庄 a[0]和村庄 a[1]有一条路，修这条路的成本价格为 a[2] .

每户之间可能有多条道路连接，但不可能自己与自己相连
'''
import sys


class Solution:
    def miniSpanningTree(self, n, m, cost):
        '''
        最小生成树：Prim算法
        1. 从任意Node开始，找到其邻边，选择权重最小的一条边解锁，激活下一个节点，并将该节点放入set
        2. 从第二节点开始，找到其邻边，选择①权重最小 && ②该边连接的点没有被解锁，把第二节点放入set，激活第三节点
        3. 依次类推，直到激活的结点列表为空，结束，返回所有激活的结点及边
        :param n:
        :param m:
        :param cost:
        :return:
        '''
        def createGraph(n, cost):
            graph = Graph()
            # 遍历所有村庄，存储到graph，0号位置存储1村庄，1号位置存储2村庄，以此类推
            for i in range(n):
                node = Node(i+1)
                graph.insertNodes(node)
            for i in range(len(cost)):
                record = cost[i]
                # node 是每一个村庄，edge是每一个村庄连接的边
                node_f = graph.nodes[record[0] - 1]
                node_t = graph.nodes[record[1] - 1]
                # from 出度++
                # node_f.o += 1
                # to 入度++
                # node_t.i += 1
                # from nexts 增加 to 点, to nexts 增加from 点
                node_f.nexts.append(node_t)
                node_t.nexts.append(node_f)
                edgef_t = Edge(node_f, node_t, record[2])
                edget_f = Edge(node_t, node_f, record[2])
                # from 边集合增加 edge, to边集合增加from
                node_f.edges.append(edgef_t)
                node_t.edges.append(edget_f)
                # graph 增加边
                graph.insertEdges(edget_f)
                graph.insertEdges(edgef_t)
            return graph

        graph = createGraph(n, cost)
        # 最小生成树：Prim算法
        # 1. 从任意Node开始，找到其邻边，选择权重最小的一条边解锁，激活下一个节点，并将该节点放入set
        # 2. 从第二节点开始，找到其邻边，选择①权重最小 && ②该边连接的点没有被解锁，把第二节点放入set，激活第三节点
        # 3. 依次类推，直到激活的结点列表为空，结束，返回所有激活的结点及边
        touchedNodes = set()
        from queue import PriorityQueue
        from itertools import count
        queue = PriorityQueue()
        res_nodes = []
        res_edges = []
        index = count(0)
        for node in graph.nodes:
            # 随便找一个点，遍历所有边，放入小根堆
            if node not in touchedNodes:
                touchedNodes.add(node)
                res_nodes.append(node)
                for e in node.edges:
                    queue.put((e.weight, next(index), e))

            while not queue.empty():
                # 获取权值最小的边
                edge = queue.get()
                # 该边对应到达的点
                to_node = edge[2].t
                # 这个点如果被激活过，跳过，否则选取该点为下一个出发的点，解锁其所有边
                if to_node in touchedNodes:
                    continue
                res_nodes.append(to_node)
                res_edges.append(edge[2])
                touchedNodes.add(to_node)
                for e in to_node.edges:
                    queue.put((e.weight, next(index), e))

            cost = 0
            for e in res_edges:
                cost += e.weight
            return cost

class Graph:
    def __init__(self):
        # list Node
        self.nodes = []
        # edges Edge
        self.edges = set()

    def insertNodes(self, node):
        self.nodes.append(node)

    def insertEdges(self, edge):
        self.edges.add(edge)

class Node:
    def __init__(self, val):
        self.val = val
        # 入度
        self.i = 0
        # 出度
        self.o = 0
        # 邻接点集合 Node
        self.nexts = []
        # 从点出发边集合 Edge
        self.edges = []

class Edge:
    def __init__(self, f, t, weight):
        # Node
        self.f = f
        # Node
        self.t = t
        # int
        self.weight = weight


if __name__ == '__main__':
    s = Solution()
    cost = s.miniSpanningTree(6,10,[[5,3,8],[1,3,6],[2,5,4],[2,3,5],[4,5,6],[3,4,3],[2,4,8],[1,2,2],[1,4,5],[5,6,2]])
    print(cost)