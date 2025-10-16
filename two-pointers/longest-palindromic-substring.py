def get_palindrome(s: str, i: int, j: int) -> int:
    res = ""
    while i >= 0 and j < (len(s)):
        if s[i] != s[j]:
            return res
        i -= 1
        j += 1
        curr = s[i+1:j]
        if len(curr) > len(res):
            res = curr
    return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr = get_palindrome(s, i=i, j=i+1)
                if len(curr) > len(res):
                    res = curr
            curr = get_palindrome(s, i=i, j=i)
            if len(curr) > len(res):
                res = curr
        return res
        