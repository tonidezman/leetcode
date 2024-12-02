import math

def can_eat(piles: List[int], mid: int, h: int) -> bool:
    counter = 0
    for bananas in piles:
        counter += math.ceil(bananas / mid)
    return counter <= h



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        res = m
        l,r = 1,m

        while l <= r:
            mid = l + (r-l) // 2
            if can_eat(piles, mid, h):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res