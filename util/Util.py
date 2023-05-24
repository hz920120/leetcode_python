class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
1. 图对象：① 点集合（map：key点编号或名称，value点对象）② 边集合（set：边对象）
2. 点对象：①. 值 ②. 入度 ③. 出度 ④. 由该点发散出去的邻接点（list：点对象）⑤. 由该点发散出去的邻边 （list：边对象） 
3. 边对象 ： ① 权重int ② 出发点对象from ③ 到达点对象to
'''
class Graph:
    def __init__(self):
        # hashmap: key -> int, value -> Node
        self.nodes = {}
        # hashset: Edge
        self.edges = set()

class Node:
    def __init__(self, value):
        self.value = value
        self.i = 0
        self.o = 0
        # list : Node
        self.nexts = []
        # list : Edge
        self.edges = []

class Edge:
    def __init__(self, weight, f, t):
        # int
        self.weight = weight
        # Node
        self.f = f
        # Node
        self.t = t