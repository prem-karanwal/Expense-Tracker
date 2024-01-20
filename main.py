import datetime

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        date = datetime.date.today()
        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("Date\t\tAmount\t\tCategory\tDescription")
        print("----------------------------------------------")
        for expense in self.expenses:
            print(f"{expense.date}\t${expense.amount}\t\t{expense.category}\t\t{expense.description}")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        category_totals = {}
        for expense in self.expenses:
            category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount

        print("Spending Patterns:")
        for category, total in category_totals.items():
            print(f"{category}: ${total}")

tracker = ExpenseTracker()

while True:
    print("\nExpense Tracking System:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Spending Patterns")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        description = input("Enter a description for the expense: ")
        tracker.add_expense(amount, category, description)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.view_spending_patterns()

    elif choice == "4":
        print("Exiting the Expense Tracking System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
