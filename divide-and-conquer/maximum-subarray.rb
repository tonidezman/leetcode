# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    return 0 if nums.empty?
    res = nums[0]
    curr = nums[0]
    1.upto(nums.size-1) do |i|
        num = nums[i]
        curr += num
        if num > curr
            curr = num
        end
        res = [res, curr].max
    end
    res
end