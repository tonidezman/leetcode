# @param {String} s
# @return {Integer}
def score_of_string(s)
    res = 0
    0.upto(s.size-2) do |i|
        res += (s[i].ord - s[i+1].ord).abs
    end
    res
end