class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms or len(rooms) == 1:
            return True

        left_rooms_size = len(rooms) - 1
        visited = [0] * len(rooms)
        visited[0] = 1
        queue = []
        for i in rooms[0]:
            queue.append(i)

        while queue:
            room = queue.pop(0)
            if visited[room] == 0:
                visited[room] = 1
                left_rooms_size -= 1
                for i in rooms[room]:
                    queue.append(i)

        return left_rooms_size == 0

