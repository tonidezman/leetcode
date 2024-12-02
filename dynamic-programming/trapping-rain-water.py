class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        curr = 0
        for i in range(len(height)):
            curr = max(curr, height[i])
            maxL[i] = curr

        maxR = [0] * len(height)
        curr = 0
        for i in range(len(height)-1,-1,-1):
            curr = max(curr, height[i])
            maxR[i] = curr

        res = 0
        for i in range(len(height)):
            bound = min(maxL[i], maxR[i])
            curr = bound - height[i]
            if curr > 0:
                res += curr
        return res
        