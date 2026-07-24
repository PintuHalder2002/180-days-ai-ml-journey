'''
Character	Picture	Grid
Say	you	have	a	list	of	lists	where	each	value	in	the	inner	lists	is	a	one-character
string,	like	this:
'''


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


'''
You	can	think	of	grid[x][y]	as	being	the	character	at	the	x-and	y-coordinates
of	a	“picture”	drawn	with	text	characters.	The	(0, 0)	origin	will	be	in	the
upper-left	corner,	the	x-coordinates	increase	going	right,	and	the	y-coordinates
increase	going	down.
Copy	the	previous	grid	value,	and	write	code	that	uses	it	to	print	the	image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
Hint:	You	will	need	to	use	a	loop	in	a	loop	in	order	to	print	grid[0][0],	then
grid[1][0],	then	grid[2][0],	and	so	on,	up	to	grid[8][0].	This	will	finish
the	first	row,	so	then	print	a	newline.	Then	your	program	should	print	grid[0]
[1],	then	grid[1][1],	then	grid[2][1],	and	so	on.	The	last	thing	your	program
will	print	is	grid[8][5].
Also,	remember	to	pass	the	end	keyword	argument	to	print()	if	you	don’t	want
a	newline	printed	automatically	after	each	print()	call.
'''




print(len(grid[0]))
print()
# len(grid) means no. of rows.
# len(grid[0]) means no. of columns
# len(grid[0]) = 6


# task is to print ...........>>>>

# (0,0)+(1,0)+...+(8,0)
# (0,1)+(1,1)+...+(8,1)
# (0,2)+(1,2)+...+(8,2)
# ....................
# ....................
# (0,2)+(1,2)+...+(8,len(grid[0]-1)

print("the desired pattern is shown below: ")
print()

print("using while loop")
print()

j=0
while j<len(grid[0]):
    for i in range(len(grid)):
        print(grid[i][j] , end = "")
    print()
    j = j + 1

print()

print("using for loop")
print()
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x] , end="")
    print()

