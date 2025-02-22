def my_reverse(arr, i, j):
    while i < j:
        # swap
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        my_reverse(nums, i=0, j=len(nums)-1)
        my_reverse(nums, i=0, j=k-1)
        my_reverse(nums, i=k, j=len(nums)-1)