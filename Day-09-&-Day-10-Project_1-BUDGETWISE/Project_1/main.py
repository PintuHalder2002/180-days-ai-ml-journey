# jai jai shree Radheshyam

import numpy as np


def show_menu():
    option_1 = "Add Expense"
    option_2 = "View Expenses"
    option_3 = "Analyze Expenses"
    option_4 = "Exit"

    print(f"\n1. {option_1}")
    print(f"2. {option_2}")
    print(f"3. {option_3}")
    print(f"4. {option_4}")


def main():
    while True:
        show_menu()

        try:
            cmd = int(input("\nChoose option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if cmd == 1:
            add_expense()

        elif cmd == 2:
            display_expense()

        elif cmd == 3:
            expense_analytics()

        elif cmd == 4:
            print("Exiting BudgetWise...")
            break

        else:
            print("Invalid option")


def add_expense():
    category = input("\nCategory: ")

    try:
        amount = int(input("Amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    # append mode creates file automatically if missing
    with open("expenses.txt", "a") as f:
        f.write(f"{category},{amount}\n")

    print("\nYour expense data is saved successfully")


def display_expense():
    print("\nHere is your complete expense details\n")

    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()

            if len(lines) == 0:
                print("No expenses added yet.")
                return

            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("No expense file found. Add expenses first.")


def expense_analytics():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()

            temp = []

            for line in lines:
                line_strip = line.strip()
                temp.append(int(line_strip.split(",")[1]))

            arr = np.array(temp)

            if len(arr) == 0:
                print("\nNo expenses found. Please add expenses first.")
                return

            print(f"\nHere is your expense list : {arr}")
            print(f"Total expense : {np.sum(arr)}")
            print(f"Highest expense : {np.max(arr)}")
            print(f"Lowest expense : {np.min(arr)}")
            print(f"Average expense : {round(np.mean(arr), 1)}")

    except FileNotFoundError:
        print("No expense file found. Add expenses first.")


if __name__ == "__main__":
    print("\n------ Welcome to BUDGETWISE ------")
    print("\nChoose your option")
    main()
