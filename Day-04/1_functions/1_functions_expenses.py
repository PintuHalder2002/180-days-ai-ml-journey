expenses_surgey = [34, 45, 27, 80]
expenses_sundar = [45, 37, 49, 110]

def find_total(list):
    total = 0
    for item in list:
        total += item
    return total

print("Total surgey's expense: ",find_total(expenses_surgey))
print("Total sundar's expense: ",find_total(expenses_sundar))
