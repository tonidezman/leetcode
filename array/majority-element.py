class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = None, 0
        for num in nums:
            if curr is None:
                curr = num
                count = 1
            elif count == 0:
                curr = num
                count = 1
            elif curr != num:
                count -= 1
            else:
                count += 1
        return curr
