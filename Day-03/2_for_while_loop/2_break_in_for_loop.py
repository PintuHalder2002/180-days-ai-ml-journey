monthly_sales = [42, 38, 33, 38, 40, 45]
months = ["Jan", "Feb", "Mar", "Apr", "May", "June"]

thresold = 35

# for sales_amount in monthly_sales:
#     if sales_amount < thresold:
#         print(f"Sales amount {sales_amount} is less than thresold")
#         break
#     else:
#         print(f"Sales_amount {sales_amount} is greater than thresold")


# a = [1,2,3]
# b = ['a', 'b', 'c', 'd']
# zip(a,b)
# <zip object at 0x0000021264751D80>
# tuple(zip(a, b))
# ((1, 'a'), (2, 'b'), (3, 'c'))

for sales_amount, month in zip(monthly_sales, months):
    print(month, sales_amount)
    if sales_amount < thresold:
        print(f"Sales amount {sales_amount} is less than the thresold in {month}")
        break
    else:
        print(f"Sales_amount {sales_amount} is greater than the thresold in {month}")




