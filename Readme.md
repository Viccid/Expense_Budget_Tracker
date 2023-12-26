# Expense Tracker

## Overview:

This expense tracker, helps in tracking daily spending within an intended budget for a month.
By creating an Expense class to store the attribute and instance of a method to keep track of the inputs.

**Expense information:** Easily record your daily expenses with detailed information such as name, category, and amount.

- **Expense Category :** Helps in Organizing daily expenses by categories, making it easy to analyse  and review spending patterns.

- **Expense Budget:** This helps in reviewing the budgets for different expense categories and tell when spending is going to exceed the required monthly budget.

## Steps to start:

    * import uuid from uuid4
    
    * import datetime from datetime


## Expense Class:

## Attributes:


* name :  The title or description of the expense.

* category : The category of expense.

* amount : The amount of money spend on expense. 

## Methods :


    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

• Initializes a new Expense instance with the provided name, amount and category.

• Returns a dictionary representation of the expense.

     __repr__(self):

• Returns a string representation of the expense.

ExpenseDatabase Class:

instance of the class:

• expenses: A list to store instances of the Expense class Methods

• init(self):

• Initializes an empty list to store expenses.

• Adds an expense to the list.

add_expense(self, expense):

    def main():

    print(f"Running The Expense tracker")

    expense_file = "expense.csv"

    budget = 40000

####   expense = get_expense_name()
     
####   update_expense_file(expense, expense_file)

####   summarize_user_expense(expense_file, budget= 40000) 
       
    print(expense)

## installations:

Python 3 was installed as this code is compatible with it.
Vscode (visual enviroment) was choosen for easy implementation of the code.
Git was easily installed for smooth remote repository to github.
## Usage:

This demonstrates creating an expenses, adding them to the ExpenseDatabase, updating an expense, removing an expense, and retrieving expenses from the database.This can be adapted and integrated, more functionality can be added based on specific requirements.

## Cloning Of Project:

Repository can be clone to your local machine with the following steps:

Open your terminal or command prompt

Type the 'cd' command on the terminal to navigate ( or specify a local where repository will be clone to on the local machine)

cd [location on local machine]   
type the git clone command, space and Path to the repository to be clone on the local machine

git clone [Path for the repository]
This is authomatically clone as required.

How To Run Expense Project Code:
Steps to run the code:

Python is installed on the machine.

Installed Visual Studio Code, from VSCode's official website.

Installed python Extensions view and rainbow column seperator.

Open the Python file (with the code for the poject)to run in VSCode.

In the top menu, find the Run option. This will run your Python script.

The output of your code will be displayed in the "Terminal" tab at the bottom of VSCode

Note:
The python script Expense and ExpenseDatabase class explained the functionality of expense tracker.

#### License: MIT License

#### Copyright (c) [2023] [Idiyeli Sunday]