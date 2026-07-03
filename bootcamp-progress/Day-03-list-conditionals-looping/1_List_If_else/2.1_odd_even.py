n = input("enter a number: ")
print(n)

if int(n) > 10 or int(n) % 2 == 0:
    print("Yay")
else:
    print("NO")

if int(n)%2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")

# Ternary operator
message = "is even" if int(n)%2 == 0 else "is odd"
print(n,message)





