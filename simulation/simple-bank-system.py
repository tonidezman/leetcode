class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        start_money_1 = None
        start_money_2 = None
        try:
            start_money_1 = self.balance[account1-1]
            if start_money_1 < money:
                return False
            start_money_2 = self.balance[account2-1]
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        except:
            if start_money_1 is not None:
                self.balance[account1-1] = start_money_1
            if start_money_2 is not None:
                self.balance[account2-1] = start_money_2
            return False

    def deposit(self, account: int, money: int) -> bool:
        try:
            self.balance[account-1] += money
            return True
        except:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        try:
            acc = self.balance[account-1]
            if acc < money:
                return False
            self.balance[account-1] -= money
            return True
        except:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)