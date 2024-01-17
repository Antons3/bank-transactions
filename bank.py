# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

def deposit(transactions, amount):
    transactions.append(amount)

def withdraw(transactions, amount):
    transactions.append(-amount)

def check_balance(transactions):
    sum(transactions)

def list():
    pass

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Amount of money:"))
        deposit(transactions, amount)
    elif choice == '2':
        amount = float(input("Amount of money:"))
        balance = sum(transactions)
        if balance >= amount:
            withdraw(transactions, amount)
        else:
            print("Not enough money:",balance)
    elif choice == '3':
        balance = sum(transactions)
        check_balance(transactions)
        print("Balance:",balance)
    elif choice == '4':
        list()
        print("List transactions",transactions)
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
