class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        curr = [0] * n
        res = 0
        while curr != target:
            update_res = True
            for i in range(n):
                if curr[i] == target[i]:
                    update_res = True
                elif curr[i] < target[i]:
                    curr[i] += 1
                    res += 1 if update_res else 0
                    update_res = False
            # res += 1 if update_res else 0
        return res
