from collections import Counter

def is_beautiful(n: int) -> bool:
    count = Counter(str(n))
    for num, count in count.items():
        if num != str(count):
            return False
    return True

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            if is_beautiful(n):
                return n