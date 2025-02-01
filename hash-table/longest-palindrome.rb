# @param {String} s
# @return {Integer}
def longest_palindrome(s)
    res = 0
    odd_taken = false
    s.chars.tally.values.sort.reverse.each do |count|
        if count.odd?
            return res if odd_taken
            odd_taken = true
        end
        res += count
    end
    res
end
