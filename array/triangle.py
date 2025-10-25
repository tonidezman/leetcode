class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = 0
        for arr in triangle:
            res += min(arr)
        return res