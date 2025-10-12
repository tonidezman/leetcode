class Solution(object):
    def removeDuplicates(self, nums):
        l, r = 0, 1
        while r < len(nums):
            if nums[r] > nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l+1

"""
0,1,2,1,1,2,2,3,3,4
    ^
          ^

"""