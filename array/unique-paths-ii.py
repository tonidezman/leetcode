class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def oob(r: int, c: int) -> bool:
            if r >= len(obstacleGrid) or c >= len(obstacleGrid[0]):
                return True
            return False

        def dp(r: int, c: int, cache: dict[tuple[int, int], int]) -> int:
            if oob(r, c) or obstacleGrid[r][c] == 1:
                return 0
            is_last_cell = r == len(obstacleGrid)-1 and c == len(obstacleGrid[0])-1
            if is_last_cell:
                return 1
            key = (r, c)
            if key in cache:
                return cache[key]
            cache[key] = dp(r+1, c, cache) + dp(r, c+1, cache)
            return cache[key]

        return dp(r=0, c=0, cache={})