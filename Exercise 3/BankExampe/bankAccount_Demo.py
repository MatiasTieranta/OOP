# File: AccountDemo
# Author: Matias Tieranta
# Description: The BankAccount class simulates a bank account
# balance is private
# two files
# two data attribute
# __str__

class BankAccount:

    # The __init__ method accepts an argument for account's balance
    # It is assigned to the __balance attribute
    def __init__(self, bal, owner):
        self.__balance = bal
        self.__owner = owner

    # The deposit method makes a deposit into the account.
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount from the account.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("error ur broke are u ?")

    # The get_balance method returns the account balance.
    def get_balance(self):
        return self.__balance

    # The get_owner method returns the bank account owner
    def get_owner(self):
        return self.__owner

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''Balance: {self.__balance} Owner: {self.__owner}'''
