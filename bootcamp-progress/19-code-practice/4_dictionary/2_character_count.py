import pprint

message = "It was a bright cold day in April and the clocks were striking thirteen."
count = {}



for character in message:
    count.setdefault(character , 0) # if the character is absent in the dictionary it's value will be 0 but if there is any value then it will disturb that value with 0.
    count[character] = count[character] + 1

print(count)
print()
pprint.pprint(count)
