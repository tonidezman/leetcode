# @param {String} s
# @return {Boolean}
def is_valid(s)
    mapping = {
        "(" => ")",
        "[" => "]",
        "{" => "}",
    }
    stack = []
    s.each_char do |brace|
        if mapping.include? brace
            stack << mapping[brace]
        else
            return false if stack.empty? || stack.pop != brace
        end
    end
    stack.length.zero?
end