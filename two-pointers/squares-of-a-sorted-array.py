class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left, right = 0, len(nums)-1
        while left <= right:
            l_square = nums[left] * nums[left]
            r_square = nums[right] * nums[right]
            if l_square > r_square:
                res.append(l_square)
                left += 1
            else:
                res.append(r_square)
                right -= 1
        res.reverse()
        return res