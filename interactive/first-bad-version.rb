# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    lo, hi = 1, n
    while lo <= hi
        mid = lo + (hi - lo) / 2
        if is_bad_version(mid)
            res = mid
            hi = mid - 1
        else
            lo = mid + 1
        end
    end
    res
end