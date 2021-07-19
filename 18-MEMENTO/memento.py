"""
Un objeto en un sistema puede pasar por multiples cambios
Hay diferentes métodos para navegar entre esos cambios
Una opción es guardar cada cambio (Command) y permitir deshacerlos
Otra opción es guardar snapshots del estado previo a un cambio para luego poder hacer roll back
"""

class Memento:
    def __init__(self, balance) -> None:
        self.balance = balance

class BankAccount:
    def __init__(self, balance = 0) -> None:
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)
    
    def restore(self, memento):
        self.balance = memento.balance
    
    def __str__(self) -> str:
        return f"Balance = {self.balance}"

if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.restore(m1)
    print(ba)

    ba.restore(m2)
    print(ba)