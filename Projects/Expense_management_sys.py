def add_expense(expenses):
    category = input("Enter your category: ")
    amount = int(input("Enter Amount: "))

    expenses[category] = expenses.get(category , 0)+ amount
    print("Expenses Added")

def view_expense(expenses):
    if not expenses:
        print("No expenses yet")
        return 

    for category , amount in expenses.items():
        print(category , ":" , amount)

def total_expense(expenses):
    total = sum(expenses.values())
    print("Total Expenses:" , total)

def main():
    expenses = {}

    while True:
        print("\n 1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expense(expenses)
        elif choice == 3:
            total_expense(expenses)
        elif choice == 4:
            print("Bye Bye")
            break
        else:
            print("Invalid choice")

main()