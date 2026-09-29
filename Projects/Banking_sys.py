def deposit(balance,amount):
    balance += amount
    print("Amount deposited")
    return balance

def withdraw(balance,amount):
    if amount <= balance:
        balance -= amount
        print("Withdraw successfully")
    else:
        print("Insufficient Balance")
    return balance

def view_balance(amount):
    print("Balance: ",amount)

def main():
    balance = 0

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter Amount: "))
            balance = deposit(balance , amount)

        elif choice == 2:
            amount = int(input("Enter Amount: "))
            balance = withdraw(balance , amount)

        elif choice == 3:
            view_balance(amount)

        elif choice == 4:
            print("BYE BYE")
            break
        else:
            print("Invalid choices")

main()


