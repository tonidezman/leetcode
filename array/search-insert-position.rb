# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
    lo, hi = 0, nums.size-1
    while lo <= hi
        mid = lo + ((hi-lo)/2).floor
        return mid if nums[mid] == target
        if target < nums[mid]
            hi = mid -1
        else
            lo = mid + 1
        end
    end
    hi + 1
end