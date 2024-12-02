class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                first = nums.pop()
                second = nums.pop()
                nums.append(second - first)
            elif token == "/":
                first = nums.pop()
                second = nums.pop()
                nums.append(int(second / first))
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            else:
                nums.append(int(token))
        return nums[-1]