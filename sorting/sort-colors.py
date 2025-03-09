def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left_boundary = 0
        right_boundary = len(nums)-1
        i = 0
        while i <= right_boundary:
            if nums[i] == 0:
                swap(nums, i, left_boundary)
                left_boundary += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, right_boundary)
                right_boundary -= 1
            
               