from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for chr in ransomNote:
            counter[chr] -= 1
            if counter[chr] < 0:
                return False
        return True
        