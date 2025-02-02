def bits(num)
    res = 0
    until num.zero?
        res += num & 1
        num >>= 1
    end
    res
end

# @param {Integer} n
# @return {Integer[]}
def count_bits(n)
    res = []
    0.upto(n) do |num|
        res << bits(num)
    end
    res
end