class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_negative(arr):
            l, r = 0, len(arr)-1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < 0:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        def find_positive(arr):
            l, r = 0, len(arr)-1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] > 0:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        idx = find_negative(nums)
        negative_len = idx + 1
        idx = find_positive(nums)
        positive_len = len(nums) - idx
        return max(negative_len, positive_len)