# imports
from turtle import *

Screen().bgpic(r"Fixed FeatherDIp UI.gif")


def goto_mouse(x, y):
    # move to mouse cursor
    penup()
    goto(x, y)
    pendown()

def drag(x, y):
    # move to mouse cursor
    if (-483 < x and 858 > x) and (-380 < y and 340 > y):
        ondrag(None)
        setheading(towards(x, y))
        goto(x, y)
        ondrag(drag)

# colors
def color_red():
    color("red")

def color_black():
    color("black")

def color_blue():
    color("blue")

def color_green():
    color("green")

def color_yellow():
    color("yellow")

def color_purple():
    color("purple")

def color_orange():
    color("orange")

def color_brown():
    color("brown")

def color_pink():
    color("pink")

def color_cyan():
    color("cyan")

def color_teal():
    color("teal")

def color_gold():
    color("gold")

def color_lime():
    color("lime")

def color_eraser():
    color("white")

# sizes
def size_1():
    pensize(1)

def size_2():
    pensize(2)

def size_3():
    pensize(3)

def size_4():
    pensize(3)

def size_5():
    pensize(5)

def size_6():
    pensize(6)

def size_7():
    pensize(7)

def size_8():
    pensize(8)

def size_9():
    pensize(9)

def size_10():
    pensize(10)

# Other
def clear_board():
    clear()

def undo_recent():
    undo()

# def instructions():
#     backward(175)
#     right(90)
#     forward(10)
#     pensize(1)
#     write("Welcome to Feather Dip! ")
#     forward(11)
#     write("to draw, click on the arrow and drag it, the arrow will also go to where ever you click on the screen")
#     forward(11)
#     write("to change colors, input any of these: r(red), b(blue), g(green), y(yellow), p(purple), d(black), o(orange), t(teal), and w(white)")
#     forward(11)
#     write("some of these also require shift to access more colors like B(brown), G(gold), and P(pink), as g and G and treated differently")
#     forward(11)
#     write("you can press (<) to undo things, and any of the number keys to change pen size")
#     forward(11)
#     write("comma (,) will start fill when drawing and period (.) wll end fill, z will clear the board")
#     forward(11)
#     write("to bring this back up, enter (?)")
#     pensize(11)

# default settings
penup()
speed("fastest")
color("black")

# color retrive
getscreen().onkey(color_black, "d")
getscreen().listen()

getscreen().onkey(color_red, "r")
getscreen().listen()

getscreen().onkey(color_blue, "b")
getscreen().listen()

getscreen().onkey(color_green, "g")
getscreen().listen()

getscreen().onkey(color_yellow, "y")
getscreen().listen()

getscreen().onkey(color_purple, "p")
getscreen().listen()

getscreen().onkey(color_orange, "o")
getscreen().listen()

getscreen().onkey(color_brown, "B")
getscreen().listen()

getscreen().onkey(color_pink, "P")
getscreen().listen()

getscreen().onkey(color_cyan, "c")
getscreen().listen()

getscreen().onkey(color_teal, "t")
getscreen().listen()

getscreen().onkey(color_gold, "G")
getscreen().listen()

getscreen().onkey(color_lime, "l")
getscreen().listen()

getscreen().onkey(color_eraser, "w")
getscreen().listen()


# Begin and end fill
getscreen().onkey(begin_fill, ",")
getscreen().listen()

getscreen().onkey(end_fill, ".")
getscreen().listen()

# size retrive
getscreen().onkey(size_1, "1")
getscreen().listen()

getscreen().onkey(size_2, "2")
getscreen().listen()

getscreen().onkey(size_3, "3")
getscreen().listen()

getscreen().onkey(size_4, "4")
getscreen().listen()

getscreen().onkey(size_5, "5")
getscreen().listen()

getscreen().onkey(size_6, "6")
getscreen().listen()

getscreen().onkey(size_7, "7")
getscreen().listen()

getscreen().onkey(size_8, "8")
getscreen().listen()

getscreen().onkey(size_9, "9")
getscreen().listen()

getscreen().onkey(size_10, "0")
getscreen().listen()


# clear board
getscreen().onkey(clear_board, "z")
getscreen().listen()

getscreen().onkey(undo_recent, "<")
getscreen().listen()

# function calls
getscreen().onclick(goto_mouse)

# instructions()
ondrag(drag)
mainloop()
