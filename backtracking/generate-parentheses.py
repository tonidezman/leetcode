class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def rec(open, close):
            if n == open == close:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                rec(open+1, close)
                stack.pop()
                
            if close < open:
                stack.append(")")
                rec(open, close+1)
                stack.pop()

        rec(open=0, close=0)
        return res