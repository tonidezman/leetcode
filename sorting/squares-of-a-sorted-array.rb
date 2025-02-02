# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
    res = []
    i, j = 0, nums.size-1
    while i <= j
        if nums[i]**2 > nums[j]**2
            res << nums[i]**2
            i += 1
        else
            res << nums[j]**2
            j -= 1
        end
    end
    res.reverse
end