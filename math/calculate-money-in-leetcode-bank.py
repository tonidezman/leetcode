class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        start = 1
        while n > 0:
            for day in range(0, 7):
                res += start + day
                n -= 1
                if n == 0:
                    return res
            start += 1
        return res
