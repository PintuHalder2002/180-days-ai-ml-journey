# x = input("Enter number 1: ")
# y = input("Enter number 2: ")

# d = 0
# try:
#     d = int(x)/int(y)
#     a = "baby yoda" + 65
# except ZeroDivisionError as ze:
#     print("Exception occured: ", ze)
#     d = -1
# except TypeError as te:
#     print("Exception occured:", te)
#     d = -1
# except Exception as e:
#     print("Generic expression, ", e)
#     d = -1

# print("Division is ", d)


# file = None

# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: The file was not found.")
# finally:
#     if file:
#         file.close()
#     print("file closed.")


class InsufficientFunds(Exception):
    pass


balance = 0

def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Amount must be positive")
    balance += amount


def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientFunds(f"Not Enough Funds. Current balance {balance}")
    balance -= amount

deposit(10)
deposit(7)
# deposit(-4)
withdraw(5)


print(balance)
