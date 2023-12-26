
# Building an Expense Tracking App To Receive Input!
# The Expense Input is Written To a File.


from uuid import uuid4
import datetime


class Expense:

    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount


    def __repr__(self):
        return f"Expense:<{self.name}, {self.category}, N{self.amount:.2f}>"   # this specifies the number of decimal places on the amount


def main():
    print(f"Running The Expense tracker")
    expense_file = "expense.csv"
    budget = 40000

    # expense = get_expense_name()
    # print(expense)
    
    # update_expense_file(expense, expense_file)

    summarize_user_expense(expense_file, budget= 40000)   



# Getting User input the expense.
    
def get_expense_name():
    
    print(f"Getting expense input")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input(f"Enter expense amount: "))

    


    # print(f"You entered {expense_name}, for {expense_amount + 200}")20G
    expense_category = [
         "Food",
         "Home",
         "Transport",
         "MobileData",
         "Misc"
    ]

    while True:
         print("Choose a category: ")
         for i, category_name in enumerate(expense_category):
              print(f"{i + 1}. {category_name}")
    
         # value_range = f"[1 -{len(expense_category)}]"
         choosen_index = int(input("Enter the category number: ") ) -1

         if choosen_index in range(len(expense_category)):
            
           choosen_category = expense_category[choosen_index]

           expense_1 = Expense(name= expense_name, category= choosen_category, amount= expense_amount)

        #  expense_1 = Expense(name= expense_name, category= expense_category, amount= expense_amount)
           
           return expense_1
         
         else:
            print("Invalid Category. Please try again")
             





# Updating the User expense file.
            
def update_expense_file(expense, expense_file):
    print(f"Updating Expense file: {expense} to {expense_file}")
        
    with open(expense_file, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


# Reading the expense file and summarise expense.


def summarize_user_expense(expense_file, budget):
    print(f"summarizing the Expense")

    expensesDatabase = []

    with open(expense_file, "r") as f:

        lines = f.readlines()
        for line in lines:

# using the line.strip to split in betwin Expenses.
            stripped_line = line.strip()
           
            expense_name, expense_category, expense_amount = stripped_line.split(",")
            print()
            print("#" * 30)
            line_expense = Expense(name=expense_name, amount= float(expense_amount), category= expense_category)

#           print(line_expense)
            expensesDatabase.append(line_expense)
    category_amount = {}

    for expense in expensesDatabase:
        key = expense.category
        if key in category_amount:
            category_amount[key] += expense.amount
        else:
            category_amount[key] = expense.amount

# Method 1:
            
#    print(category_amount)  

# Alternatively we can use method 2:
    print("Category of Expenses")
    for key, amount in category_amount.items():
        print(f" {key}, N{amount:.2f}")


#  To calculate total amount spent from the monthly budget and amount remainin.

        amount_spent = sum([expense.amount for expense in expensesDatabase])
        print(f" Total amount spent: N{amount_spent:.2f} for the month")
        budget_amount_left = budget - amount_spent

        print(f"Budget Amount Lelf: N{budget_amount_left:.2f}")

#   print(expensesDatabase)

# # This will print result the amount spent on each category.
# # Key will be category while amount is value



   
if __name__ == "__main__":
        main()
    
    