class StudentBudget:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = {
            "Rent": 0,
            "Food": 0,
            "Transport": 0,
            "Books": 0,
            "Entertainment": 0,
            "Others": 0
        }

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            print("Invalid category. Please choose a valid expense category.")

    def total_expenses(self):
        return sum(self.expenses.values())

    def is_within_budget(self):
        return self.total_expenses() <= self.budget

    def display_expenses(self):
        print("Expense Summary:")
        for category, amount in self.expenses.items():
            print(f"{category}: TK {amount}")
        print(f"Total Expenses: TK {self.total_expenses()}")
        print("Within Budget" if self.is_within_budget() else "Over Budget")

budget = StudentBudget(9500)
budget.add_expense("Rent", 1500)
budget.add_expense("Food", 5000)
budget.add_expense("Transport", 1000)
budget.add_expense("Books", 1200 )
budget.add_expense("Entertainment", 300)
budget.add_expense("Others", 500)

budget.display_expenses()
