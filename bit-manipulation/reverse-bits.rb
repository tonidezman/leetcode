# @param {Integer} n, a positive integer
# @return {Integer}
def reverse_bits(n)
    s = n.to_s(2)
    res = [s]
    s.size.upto(32-1) { res.unshift('0') }
    res = res.join
    res.reverse.to_i(2)
end