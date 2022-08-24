class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 保存所有入度为0的点，依次解锁，解锁后抹除其影响的点的入度
        # 没有找入度为0的点，break，判断所有点是否解锁，是true，否false
        def createGraph(numCourses, prerequisites):
            g = Graph()
            course_list = []
            for i in range(numCourses):
                node = Node(i)
                course_list.append(i)
                g.nodes.append(node)

            for i in range(len(prerequisites)):
                relation = prerequisites[i]
                # node1 depends node2
                node2 = g.nodes[relation[0]]
                node1 = g.nodes[relation[1]]
                node1.o += 1
                node1.nexts.append(node2)
                node2.i += 1
                edge = Edge(node1, node2)
                node1.edges.append(edge)
                g.edges.append(edge)
            return g, course_list

        graph, course_list = createGraph(numCourses, prerequisites)
        queue = []
        for node in graph.nodes:
            if node.i == 0:
                queue.append(node)

        while queue:
            node = queue.pop()
            print('当前课程: '+str(node.val))
            course_list.remove(node.val)
            if node.o == 0:
                continue
            for next in node.nexts:
                next.i -= 1
                if next.i == 0:
                    queue.append(next)

        return len(course_list) == 0


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

class Node:
    def __init__(self, val):
        self.val = val
        self.i = 0
        self.o = 0
        self.nexts = []
        self.edges = []

class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(4, [[1,0], [2,1], [3,2], [1,3]]))