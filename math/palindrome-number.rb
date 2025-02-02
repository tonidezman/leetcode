# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  return false if x.negative?

  mask = 1
  while x > (10 * mask)
    mask *= 10
  end

  while x > 0
    lsd = x % 10
    msd = x / mask
    return false if lsd != msd
    x = x % mask
    x = x / 10
    mask /= 100
  end
  true
end