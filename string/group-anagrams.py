from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            res[sorted_word(word)].append(word)
        return res.values()

def sorted_word(word: str) -> str:
    return "".join(sorted(word))
