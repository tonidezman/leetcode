class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while n:
            n >>= 1
            x <<= 1
            x |= 1
        return x >> 1
        

"""
1010
1111
"""