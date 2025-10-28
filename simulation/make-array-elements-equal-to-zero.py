def do_stuff(nums: List[int], start: int, direction: int) -> int:
    zero_counts = nums.count(0)
    i = start
    while zero_counts != len(nums) and i >= 0 and i < len(nums):
        if nums[i] == 0:
            i += direction
        else:
            nums[i] -= 1
            if nums[i] == 0:
                zero_counts += 1
            direction = 1 if direction == -1 else -1
            i += direction
    return 1 if zero_counts == len(nums) else 0


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        for i, count in enumerate(nums):
            if count == 0:
                res += do_stuff(nums[:], i, direction=1)
                res += do_stuff(nums[:], i, direction=-1)
        return res