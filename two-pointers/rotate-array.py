class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        my_reverse(nums, 0, len(nums)-1)
        my_reverse(nums, 0, k-1)
        my_reverse(nums, k, len(nums)-1)

def my_reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1