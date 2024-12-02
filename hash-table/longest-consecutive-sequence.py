class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        visited = set()
        res = 0
        for num in nums:
            curr = 1
            if (num -1) not in seen:
                while (num + 1) in seen:
                    curr += 1
                    num += 1
                res = max(res, curr)
        return res