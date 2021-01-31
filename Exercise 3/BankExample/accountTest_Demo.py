# File: accountTest_demo.py
# Author: Matias Tieranta
# Description_: This program demonstrates the BankAccount class

import bankAccount_Demo


def main():
    # Get the starting balance
    start_bal = float(input('enter the starting balance: '))

    # Get the owner
    owner = input('Enter the owner: ')

    # Create a BankAccount object.
    savings = bankAccount_Demo.BankAccount(start_bal, owner)

    # Display the balance
    print(savings)

    # Get the amount to deposit
    amount = float(input('Enter the amount to be deposited: '))
    savings.deposit(amount)

    # Display the balance
    print(savings)

    # Get the amount to withdraw
    amount = float(input('Enter the amount to be deposited: '))
    savings.withdraw(amount)

    # Display the balance
    print(savings)


main()
