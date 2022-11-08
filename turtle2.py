#draw a Skycrapper using turtle package
ndim=4
import turtle
for i in range(1,ndim+1):
	for g in range(ndim-i):
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(10)
	
	for j in range(i):
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(10)
	turtle.width(5)
	if i%2==1:
		turtle.color("blue")
	else:
		turtle.color("red")
	turtle.forward(120)
	turtle.right(90)
	turtle.forward(10)
	turtle.right(90)
	
turtle.color("green")
for l in range(ndim):
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(100)
	turtle.right(90)
1
