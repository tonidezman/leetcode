# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    seen = {}
    nums.each_with_index do |num, i|
        other = target - num
        if seen.include? other
            return [seen[other], i]
        else
            seen[num] = i
        end
    end
end