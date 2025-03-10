class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l,r=0,len(nums)-1

        while l <= r:
            mid = l + ((r-l)//2)
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res