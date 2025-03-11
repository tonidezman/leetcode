# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, hi = 0, n
        while low <= hi:
            mid = low + (hi - low) // 2
            curr_guess = guess(mid)
            if curr_guess == 0:
                return mid
            elif curr_guess == -1:
                hi = mid - 1
            else:
                low = mid + 1
        