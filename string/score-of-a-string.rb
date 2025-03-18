# @param {String} s
# @return {Integer}
def score_of_string(s)
    0.upto(s.size-2).reduce(0) { |acc, i| acc + (s[i].ord - s[i+1].ord).abs }
end