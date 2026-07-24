birthdays = {'Alice': 'Apr 1' , 'Bob': 'Dec 12' , 'Carol': 'March 4'}

# while True:
#     print("Enter a name: (blank to quit)")
#     name = input()

#     if name == '':
#         break


#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for' + name)
#         print('What is their birthday?')

#         bday = input()
#         birthdays[name] = bday

#         print('Birthday database updated')

print(birthdays)


# Dictionary methods
for i in birthdays.keys():
    print(i)

for v in birthdays.values():
    print(v)

for item in birthdays.items():
    print(item)



picnicitems = {'apples': 5 , 'cups': 2}


# Dictionary get methods
print("I am bringing " + str(picnicitems.get('cups' , 0)) + " cups")

print("I am bringing " + str(picnicitems.get('plates' , 5)) + " cups")

picnicitems.setdefault('color' , 'black')

print(picnicitems)
picnicitems['color'] = 'red'
print(picnicitems)
