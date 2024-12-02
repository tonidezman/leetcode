class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and h <= stack[-1][1]:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights)-i))
        
        return res