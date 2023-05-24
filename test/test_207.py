


class Solution(object):
    def cal_value(self, z_node, zero_in_nodes, touchedNodes):
        # the in value of nexts -= 1
        for next_node in z_node.nexts:
            next_node.i -= 1
            z_node.o -= 1
            if next_node.i == 0:
                zero_in_nodes.add(next_node)


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def createGraph(numCourses, prerequisites):
            # courses -> nodes
            graph = Graph()
            for course in range(numCourses):
                node = Node(course)
                graph.nodes.append(node)
            for m in range(len(prerequisites)):
                fr, to = graph.nodes[prerequisites[m][1]], graph.nodes[prerequisites[m][0]]
                fr.o += 1
                to.i += 1
                edge = Edge(fr, to, 0)
                fr.nexts.append(to)
                fr.edges.append(edge)
                to.edges.append(edge)
                graph.edges.add(edge)
            return graph

        g = createGraph(numCourses, prerequisites)
        touchedNodes = []
        # find a node which in value is zero
        zero_in_nodes = set()
        for node in g.nodes:
            touchedNodes.append(node)
            if node.i == 0:
                zero_in_nodes.add(node)

        while zero_in_nodes:
            curr_z_node = zero_in_nodes.pop()
            touchedNodes.remove(curr_z_node)
            self.cal_value(curr_z_node, zero_in_nodes, touchedNodes)

        return False if touchedNodes else True

class Graph:
    def __init__(self):
        self.edges = set()
        self.nodes = []

    def insertEdges(self, edge):
        self.edges.add(edge)

    def insertNodes(self, node):
        self.nodes.append(node)


class Node:
    '''
    in, out, val, edge, nexts
    '''
    def __init__(self, val):
        self.val = val
        self.i = 0
        self.o = 0
        self.edges = []
        self.nexts = []

class Edge:
    '''
    from, to, weight
    '''
    def __init__(self, f, t, weight):
        self.f = f
        self.t = t
        self.weight = weight


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))