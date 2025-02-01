# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    x = s.downcase.scan(/[a-z0-9]/).join
    x == x.reverse
end
