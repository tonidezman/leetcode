# @param {String} s
# @return {Integer}
def roman_to_int(s)
    mapping = {
        "I" => 1,
        "V" => 5,
        "X" => 10,
        "L" => 50,
        "C" => 100,
        "D" => 500,
        "M" => 1000,
    }

    res = 0
    s.each_char.with_index do |c, i|
        curr = mapping[c]
        if i < (s.size-1)
            next_c = mapping[s[i+1]]
        else
            next_c = mapping[c]
        end
        if curr < next_c
            res -= curr
        else
            res += curr
        end
    end
    res
end