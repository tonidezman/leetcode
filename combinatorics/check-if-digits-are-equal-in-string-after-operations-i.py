def do_stuff(s: str) -> str:
    if len(s) == 2:
        return s
    res = []
    i = 0
    for i in range(1, len(s)):
        res.append(str((int(s[i-1]) + int(s[i])) % 10))
    return "".join(res)


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = do_stuff(s)
        return s[0] == s[1]