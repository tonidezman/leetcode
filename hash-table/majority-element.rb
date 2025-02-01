# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    res = nums[0]
    count = 1
    (1..nums.size-1).each do |i|
        curr = nums[i]
        if curr == res
            count += 1
        else
            count -= 1
            if count == 0
                res = curr
                count = 1
            end
        end
    end
    res
end