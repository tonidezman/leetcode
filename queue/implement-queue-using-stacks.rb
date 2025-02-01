class MyQueue
    attr_accessor :stack1, :stack2

    def initialize()
        @stack1 = []
        @stack2 = []
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        stack1 << x
    end


=begin
    :rtype: Integer
=end
    def pop()
        return stack2.pop if !stack2.empty?
        until stack1.empty?
            stack2 << stack1.pop
        end
        stack2.pop
    end


=begin
    :rtype: Integer
=end
    def peek()
        stack2[-1] || stack1[0]
    end


=begin
    :rtype: Boolean
=end
    def empty()
        stack1.empty? && stack2.empty?
    end

end

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue.new()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()