"""
Command:
=> Ordinary statements are perishable:
     .Cannot undo member assignment
     .Cannot directly serialize a sequence of actions (calls)

=> Want an object that represents an operation

Es un objeto que representa una instruccion para realizar una accion. Contiene toda la informacion
necesaria para llevar a cabo la accion
"""
from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0) -> None:
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdraw {amount}, balance = {self.balance}")

            return True
        return False

    def __str__(self) -> str:
        return f"Balance = {self.balance}"

class Command(ABC):
    def invoke(self):
        pass
    
    def undo(self):
        pass
    
class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1


    def __init__(self, account, action, amount) -> None:
        self.action = action
        self.account = account
        self.amount = amount
        self.succes = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.succes = True
        elif self.action == self.Action.WITHDRAW:
            self.succes = self.account.withdraw(self.amount)


    def undo(self):
        if not self.succes:
            return
            
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)

if __name__ == "__main__":
    ba = BankAccount()

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print(f"After deposit of 100: {ba}")

    cmd.undo()
    print(f"100 deposit undone: {ba}")

    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print(f"After impossible withdrawel: {ba}")
    illegal_cmd.undo()
    print(f"Balance {ba} ")