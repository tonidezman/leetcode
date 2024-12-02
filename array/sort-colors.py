def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l_boundary = 0
        r_boundary = len(nums)-1
        i = 0
        while i <= r_boundary: 
            if nums[i] == 0:
                swap(nums, i, l_boundary)
                l_boundary += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, r_boundary)
                r_boundary -= 1