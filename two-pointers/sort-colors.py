class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1
        
        i = 0
        while i < len(nums):
            for j in range(len(counter)):
                for _ in range(counter[j]):
                    nums[i] = j
                    i += 1
        