# @param {String} s
# @return {Integer}
def longest_palindrome(s)
    res = 0
    odd_count_present = false
    s.chars.tally.values.each do |count|
        if count.even?
            res += count
        else
            res += count - 1
            odd_count_present = true
        end
    end
    res += 1 if odd_count_present
    res
end
