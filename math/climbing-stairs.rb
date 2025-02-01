# @param {Integer} n
# @return {Integer}
def climb_stairs(n, step=0, memo={})
    return memo[step] if memo.include?(step)
    return 0 if step > n
    return 1 if step == n
    memo[step] = climb_stairs(n, step + 1, memo) + climb_stairs(n, step + 2, memo)
    return memo[step]
end