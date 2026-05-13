'''
1. Bank Account System

Create a class BankAccount.

Data Members:
accountHolderName
accountNumber
balance

Functions:
deposit()
withdraw()
displayBalance()
Real World:

A customer deposits and withdraws money from a bank account.
'''
print(f'Problem Statement:\n {__doc__}')
class BankAccount:
    def __init__(self,accountHolderName, accountNumber, balance):
        self.accountHolderName = accountHolderName
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f'Credited {money}')
        print(f'Total Balance is {self.balance}')

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            print(f"Withdraw: {cash}")
            print(f'Remaining balance is {self.balance}')
        else:
            print("Insufficient balance")

    def displayBalance(self):
        print('-------------------------------------------------------')
        print(f'Account Holder Name: {self.accountHolderName}')
        print(f'Account Number: {self.accountNumber}')
        print(f'Account Balance: {self.balance}')
        print('--------------------------------------------------------')

customer1 = BankAccount("Balkrushna Naik", 292889560945, 20000)
customer1.deposit(2000)
customer1.withdraw(3000)
customer1.displayBalance()


