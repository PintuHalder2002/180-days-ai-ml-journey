'''
The	Collatz	Sequence
Write	a	function	named	collatz()	that	has	one	parameter	named	number.	If
number	is	even,	then	collatz()	should	print	number // 2	and	return	this	value.
If	number	is	odd,	then	collatz()	should	print	and	return	3 * number + 1.
Then	write	a	program	that	lets	the	user	type	in	an	integer	and	that	keeps	calling
collatz()	on	that	number	until	the	function	returns	the	value	1.	(Amazingly
enough,	this	sequence	actually	works	for	any	integer—sooner	or	later,	using	this
sequence,	you’ll	arrive	at	1!	Even	mathematicians	aren’t	sure	why.	Your
program	is	exploring	what’s	called	the	Collatz	sequence,	sometimes	called	“the
simplest	impossible	math	problem.”)
Remember	to	convert	the	return	value	from	input()	to	an	integer	with	the
int()	function;	otherwise,	it	will	be	a	string	value.
Hint:	An	integer	number	is	even	if	number % 2 == 0,	and	it’s	odd	if	number %
2 == 1.
The	output	of	this	program	could	look	something	like	this:
Enter number:
3
10
5
16
8
4
2
1
Input	Validation
Add	try	and	except	statements	to	the	previous	project	to	detect	whether	the
user	types	in	a	noninteger	string.	Normally,	the	int()	function	will	raise	a
ValueError	error	if	it	is	passed	a	noninteger	string,	as	in	int('puppy').	In	the
except	clause,	print	a	message	to	the	user	saying	they	must	enter	an	integer.
'''


# Write your code here :-)
def collatz(number):
    if number % 2 == 0:
        x = number // 2
        print(x)
    else:
        x = 3 * number + 1
        print(x)
    return x


def collatz_seq():
    user_inp = input("Enter the number: ")
    desired_number = user_inp

    while desired_number != 1:
        try:
            desired_number = collatz(int(desired_number))
        except ValueError:
            print("Input must be an  integer.")

            break

    return desired_number


collatz_seq()

'''
y  = collatz(3)
print(y)'''
