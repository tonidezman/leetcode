# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    smallest = strs.map(&:size).min
    res = []
    0.upto(smallest) do |i|
        letter = strs[0][i]
        strs.each do |word|
            return res.join if word[i] != letter
        end
        res << letter
    end
    res.join
end