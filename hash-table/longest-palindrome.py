from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        is_odd = False
        for _, count in counter.items():
            if count % 2 == 0:
                res += count
            else:
                is_odd = True
                res += count - 1
        if is_odd:
            res += 1
        return res
        