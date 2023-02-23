from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

def go_left():
    jim.left(20)

def go_right():
    jim.right(20)

def go_forwards():
    jim.forward(50)

def go_backwards():
    jim.backward(50)

def clear_screen():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

screen.listen()
screen.onkey(key="w", fun=go_forwards)
screen.onkey(key="s", fun=go_backwards)
screen.onkey(key="a", fun=go_left)
screen.onkey(key="d", fun=go_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

 