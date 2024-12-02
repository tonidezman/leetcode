class Solution:
    def isPalindrome(self, x: int) -> bool:
        if  x < 0:
            return False

        mask = 1
        while x >= 10 * mask:
            mask *= 10
        
        while x > 0:
            lsd = x % 10
            msd = x // mask
            if lsd != msd:
                return False
            x %= mask
            x //= 10
            mask //= 100
        return True