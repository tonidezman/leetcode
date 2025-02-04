# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
    nums.sort!
    res = []
    0.upto(nums.size-1) do |i|
        next if i > 0 and nums[i] == nums[i-1]
        l = i+1
        r = nums.size-1
        while l < r
            curr_sum = nums[i] + nums[l] + nums[r]
            puts curr_sum
            if curr_sum == 0
                res << [nums[i], nums[l], nums[r]]
                l += 1
                while nums[l] == nums[l-1] and l < r
                    l += 1
                end
            elsif curr_sum > 0
                r -= 1
            else
                l += 1
            end
        end
    end
    res
end