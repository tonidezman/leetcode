# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    res = 0
    nums.each do |num|
        res ^= num
    end
    res
end