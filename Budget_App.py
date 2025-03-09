

def add_expense(Expenses,Description,Amount):
        Expenses.append({"Description": Description, "Amount": Amount})
        print("Added expenses: ", Description, "Amount: ", Amount)


def get_balance(budget,Expenses):
    total_expense = sum(expense['Amount'] for expense in Expenses)
    return budget - total_expense

def show_budget_detail(budget,Expenses):
    print(f"Total budget: {budget}")
    for expense in Expenses:
        print(f"expenses: {expense['Description']}, {expense['Amount']}")
    print("Total Balance: ",get_balance(budget,Expenses))
def main():
    print("Welcome to your Budget App.")
    budget = int(input("Please enter your initial budget: "))
    Expenses = []

    while True:
        print("\n" + "What would you like to do?")
        print("1. Add an expense: ")
        print("2. Show budget details: ")
        print("3. Exit: ")
        choice = int(input("Enter your choice (1/2/3): "))
        if choice == 1:
            while True:
                Description = input("Enter expense description: ")
                Amount = float(input("Enter expense amount: "))
                add_expense(Expenses, Description, Amount)
                More = input("Do you want add more expenses? type 'yes': ")
                if More.lower() != 'yes':
                    break
                else:
                    print("Okay!")

        elif choice == 2:
            show_budget_detail(budget,Expenses)
        elif choice == 3:
            print("Thank you for using Our Budget App!")
            break
        else:
            print("Invalid Input!")
            print("Please Try Again")

main()