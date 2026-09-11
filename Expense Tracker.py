class ExpenseTracker:
    
    def __init__(self):
        self.expenses= []


    def add_expense(self):
        try:
            amount=float(input("Enter expense Amount:"))
            category=input("Enter category:")
            description=input("Enter description:")

            expense={
                "amount":amount,
                "category":category,
                "description":description,
                }

            
            self.expenses.append(expense)
            print("expense added successfully!")

        except ValueError:
            print("Invalid amount! please enter a number:")
    

# To view expenses

    def view_expenses(self):
        if not self.expenses:
            print("No Expense Found.")
            return

        print("\n----Expense List----")


        for expense in self.expenses:
            print("Amount:", expense["amount"])
            print("Category:",expense["category"])
            print("description", expense["description"])
            print("----------------------------")

 # Total expense

    def total_expense(self):
        
        total=0

        for expense in self.expenses:
            total=total+expense["amount"]
            
        print("Total expense:",total)


    def run(self):


        while True:

            print("\n====Expense Tracker list====")
            print("1. add_expense")
            print("2. view_expenses")
            print("3. Total_expense")
            print("4. Exit")

            choice=input("Enter your Choice:")


            if choice=="1":
                self.add_expense()

            elif choice== "2":
                self.view_expenses()


            elif choice== "3":
                self.total_expense()

            elif choice== "4":
                print("Thank you!")
                break
            else:
                print("invalid choice")

# Create object
tracker = ExpenseTracker()

# Start the program
tracker.run()



        
    

        


















    

