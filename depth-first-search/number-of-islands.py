class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    mark(grid, row, col, visited)
        return res

def mark(grid, row, col, visited):
    if oob(grid, row, col) or grid[row][col] == "0" or (row, col) in visited:
        return
    visited.add((row, col))
    mark(grid, row+1, col, visited)
    mark(grid, row-1, col, visited)
    mark(grid, row, col+1, visited)
    mark(grid, row, col-1, visited)

def oob(grid, row, col):
    if row < 0 or col < 0:
        return True
    if row >= len(grid) or col >= len(grid[0]):
        return True
    return False