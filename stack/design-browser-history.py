class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        curr = self.curr
        while curr and steps > 0:
            if curr.val == self.homepage:
                self.curr = curr
                return curr.val
            curr = curr.prev
            steps -= 1
        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr.next and steps > 0:
            curr = curr.next
            steps -= 1
        self.curr = curr
        return curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)