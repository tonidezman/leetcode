from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def oob(r: int, c: int) -> bool:
            if r < 0 or c < 0:
                return True
            if r >= len(grid) or c >= len(grid[0]):
                return True
            return False

        queue = deque([(0, 0, 1)])
        visited = set()
        while queue:
            r, c, distance = queue.popleft()
            if oob(r, c) or (r, c) in visited or grid[r][c] == 1:
                continue
            visited.add((r, c))
            is_last_cell = r == len(grid)-1 and c == len(grid[0])-1
            if is_last_cell:
                return distance
            queue.append((r+1, c, distance+1))
            queue.append((r-1, c, distance+1))
            queue.append((r, c+1, distance+1))
            queue.append((r, c-1, distance+1))
            queue.append((r-1, c-1, distance+1))
            queue.append((r-1, c+1, distance+1))
            queue.append((r+1, c+1, distance+1))
            queue.append((r+1, c-1, distance+1))
        return -1