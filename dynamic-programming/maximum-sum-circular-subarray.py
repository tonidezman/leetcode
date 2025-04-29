class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        currMax = 0
        globalMin = float('inf')
        currMin = 0
        total = 0
        for num in nums:
            currMax = max(num, currMax+num)
            globalMax = max(globalMax, currMax)
            total += num
            currMin = min(num, currMin+num)
            globalMin = min(globalMin, currMin)
        if globalMax < 0:
            return globalMax
        return max(globalMax, total - globalMin)
