# @param {Integer} n
# @return {Boolean}
def is_happy(n)
    1.upto(10) do
        return true if n == 1
        n = n.to_s.split('').map { |n| n.to_i ** 2}.sum
    end
    false
end