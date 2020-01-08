import turtle

myturtle = turtle.Turtle()
mywin = turtle.Screen()

def drawturtle(myturtle, linelen):
	if linelen > 0:
		myturtle.forward(linelen)
		myturtle.right(90)
		drawturtle(myturtle, linelen-5)

if __name__ == '__main__':
	drawturtle(myturtle, 100)
	mywin.exitonclick()
