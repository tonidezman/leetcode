class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # swap
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

 