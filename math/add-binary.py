class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res = []
        carry = 0
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            curr = digitA + digitB + carry
            res.append(f"{curr % 2}")
            carry = curr // 2
        if carry:
            res.append(str(carry))
        return "".join(reversed(res))

