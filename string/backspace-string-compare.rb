
def calculate(s)
    stack = []
    s.each_char do |c|
        if c == "#"
            next if stack.empty?
            stack.pop
        else
            stack << c
        end
    end
    stack
end

# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    calculate(s) == calculate(t)
end