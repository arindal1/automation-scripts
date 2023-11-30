import streamlit as st
import json
from datetime import datetime

# Function to load expense data from a JSON file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

# Function to save expense data to a JSON file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)

# Function to log expenses to a text file
def log_expense(category, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {category}: ${amount}\n"
    with open("expense_log.txt", "a") as log_file:
        log_file.write(log_entry)

# Function to add a new expense
def add_expense(expenses, category, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_expense = {"timestamp": timestamp, "category": category, "amount": amount}
    expenses.append(new_expense)
    save_expenses(expenses)
    log_expense(category, amount)
    st.success("Expense added successfully!")

# Function to view expense history
def view_expenses(expenses):
    if not expenses:
        st.warning("No expenses recorded.")
    else:
        st.write("Expense History:")
        for expense in expenses:
            st.write(
                f"{expense['timestamp']} - {expense['category']}: ${expense['amount']}"
            )
        total_expenses = sum(expense["amount"] for expense in expenses)
        st.write(f"Total Expenses: ${total_expenses}")

# Function to clear expenses
def clear_expenses():
    with open("expenses.json", "w") as file:
        file.write("[]")
    with open("expense_log.txt", "w") as log_file:
        log_file.write("")
    st.success("Expenses cleared successfully!")

# Streamlit app
def main():
    st.title("Expense Tracker")

    expenses = load_expenses()

    option = st.sidebar.selectbox("Select an option", ["Add Expense", "View Expenses", "Clear Expenses"])

    if option == "Add Expense":
        st.header("Add Expense")
        category = st.text_input("Enter expense category:")
        amount = st.number_input("Enter expense amount:")
        if st.button("Add Expense"):
            if not category or amount <= 0:
                st.warning("Please enter valid category and amount.")
            else:
                add_expense(expenses, category, amount)

    elif option == "View Expenses":
        st.header("View Expenses")
        view_expenses(expenses)

    elif option == "Clear Expenses":
        st.header("Clear Expenses")
        if st.button("Clear All Expenses"):
            clear_expenses()

if __name__ == "__main__":
    main()
