# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    lo, hi = 0, nums.size-1
    while lo <= hi
        mid = lo + (hi - lo) / 2
        if nums[mid] == target
            return mid
        elsif target > nums[mid]
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    -1
end