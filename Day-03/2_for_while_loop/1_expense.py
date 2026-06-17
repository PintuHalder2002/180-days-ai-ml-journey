expenses = [1200, 1300, 1500, 1700]
total_expense = 0

for expense in expenses:
    total_expense = total_expense + expense
print(total_expense)


# for i in range(len(expenses)):
#     expense = expenses[i]
#     print(f"Month {i+1}, Expense: {expense}")
#     total_expense += expense

# for i, expense in enumerate(expenses):
#     print(f"Month {i+1}, Expense: {expense}")
#     total_expense += expense

print(f"Total Expense: {total_expense}")

