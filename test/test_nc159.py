'''
一个有 n 户人家的村庄，有 m 条路相互连接着。村里现在要修路，每条路都有一个成本价格，现在请你帮忙计算下，最少需要花费多少钱，就能让这 n 户人家连接起来。

cost 为一个二维数组，每个元素是一个长度为 3 的一维数组 aa ， a[0] 和 a[1] 表示村庄 a[0]和村庄 a[1]有一条路，修这条路的成本价格为 a[2] .

每户之间可能有多条道路连接，但不可能自己与自己相连
'''
import sys
class Solution:
    def miniSpanningTree(self, n, m, cost):

        def createGraph(n, cost):
            graph = Graph()
            for i in range(n):
                node = Node(i+1)
                graph.insertNode(node)

            for h in range(len(cost)):
                record = cost[h]
                node_f = graph.nodes[record[0] - 1]
                node_t = graph.nodes[record[1] - 1]
                weight = record[2]

                node_f.nexts.append(node_t)
                node_t.nexts.append(node_f)
                e_ft = Edge(weight, node_f, node_t)
                e_tf = Edge(weight, node_t, node_f)
                node_f.edges.append(e_ft)
                node_t.edges.append(e_tf)
                graph.insertEdge(e_ft)
                graph.insertEdge(e_tf)

            return graph
        graph = createGraph(n, cost)

        # 最小生成树：Prim算法
        # 1. 从任意Node开始，找到其邻边，选择权重最小的一条边解锁，激活下一个节点，并将该节点放入set
        # 2. 从第二节点开始，找到其邻边，选择①权重最小 && ②该边连接的点没有被解锁，把第二节点放入set，激活第三节点
        # 3. 依次类推，直到激活的结点列表为空，结束，返回所有激活的结点及边
        touchedNodes = set()
        for node in graph.nodes:
            touchedNodes.add(node)
        start_node = touchedNodes.pop()
        total_cost = 0
        while touchedNodes:
            # 任意点连接的所有边
            nexts = start_node.edges
            min_wei = sys.maxsize
            selected_node = None
            for edge in nexts:
                if edge.weight < min_wei and edge.t in touchedNodes:
                    selected_node = edge.t
                    min_wei = edge.weight
            if not selected_node:
                touchedNodes.remove(start_node)
                continue
            else:
                start_node = selected_node
                touchedNodes.remove(selected_node)
                total_cost += min_wei

        return total_cost

class Graph:
    '''
           nodes
           edges
    '''

    def __init__(self):
        self.nodes = []
        self.edges = set()

    def insertNode(self, node):
        self.nodes.append(node)

    def insertEdge(self, edge):
        self.edges.add(edge)


class Node:
    '''
    val, edges, nexts, in, out
    '''
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.nexts = []
        self.i = 0
        self.o = 0

class Edge:
    '''
    weight, from ,to
    '''
    def __init__(self, weight, f, t):
        self.weight = weight
        self.f = f
        self.t = t

if __name__ == '__main__':
    s = Solution()
    cost = s.miniSpanningTree(6,10,[[5,3,8],[1,3,6],[2,5,4],[2,3,5],[4,5,6],[3,4,3],[2,4,8],[1,2,2],[1,4,5],[5,6,2]])
    print(cost)