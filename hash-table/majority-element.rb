# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    a = nums[0]
    counter = 1
    1.upto(nums.size-1) do |i|
        curr = nums[i]
        if curr == a
            counter += 1
        else
            counter -= 1
            if counter == 0
                a = curr
                counter = 1
            end
        end
    end
    a
end