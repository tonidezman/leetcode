class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        braces = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for brace in s:
            if brace in braces:
                stack.append(braces[brace])
            else:
                if len(stack) == 0 or stack.pop() != brace:
                    return False
        return len(stack) == 0
