# @param {Integer} n
# @return {Integer}
def climb_stairs(n, step=0)
    return 0 if step > n
    return 1 if step == n
    return climb_stairs(n, step + 1) + climb_stairs(n, step + 2)
end