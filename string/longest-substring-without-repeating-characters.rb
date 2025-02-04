# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    res = 0
    l = 0
    char_set = Set.new
    s.each_char.with_index do |c, r|
        while char_set.include?(c)
            char_set.delete(s[l])
            l += 1
        end
        char_set.add(c)
        res = [res, r-l+1].max
    end
    res
end
