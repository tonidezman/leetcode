class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.stack_back = []
        self.stack_forw = []
        

    def visit(self, url: str) -> None:
        self.stack_back.append(url)
        self.stack_forw = []

    def back(self, steps: int) -> str:
        while self.stack_back and steps > 0:
            steps -= 1
            self.stack_forw.append(self.stack_back.pop())
        return (self.stack_back and self.stack_back[-1]) or self.homepage

    def forward(self, steps: int) -> str:
        while self.stack_forw and steps > 0:
            self.stack_back.append(self.stack_forw.pop())
            steps -= 1
        return self.stack_back[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)