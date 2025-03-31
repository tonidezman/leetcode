from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        curr_counter = Counter()
        left = right = 0
        res = []
        while right < len(s):
            curr_counter[s[right]] += 1
            if right - left + 1 == len(p):
                if curr_counter == counter_p:
                    res.append(left)
                curr_counter[s[left]] -= 1
                left += 1
            right += 1
        return res
        