class BankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount_withdraw: int) -> None:
        if 0 < amount_withdraw <= self.balance:
            self.balance -= amount_withdraw

    def topup(self, amount_topup: int) -> None:
        if amount_topup > 0:
            self.balance += amount_topup

    def __str__(self) -> str:
        return f"Your account balance is: {self.balance}"
