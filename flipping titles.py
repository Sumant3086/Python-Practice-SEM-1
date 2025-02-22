
from random import *
from turtle import *

screen = Screen()


screen.bgcolor("yellow")




def Square(x, y):
    up()
    goto(x, y)
    down()
    color('white', 'green')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()



def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)




def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200



def click(x, y):
    spot = Numbering(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    clear()
    goto(0, 0)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = Coordinates(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 10)


tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


shuffle(tiles)
tracer(False)
onscreenclick(click)
draw()
done()



#code by Sumant
