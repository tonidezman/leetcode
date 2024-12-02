class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for brace in s:
            if brace in mapping:
                stack.append(mapping[brace])
            else:
                if len(stack) == 0 or brace != stack.pop():
                    return False
        return len(stack) == 0
