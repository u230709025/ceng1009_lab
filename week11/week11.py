import turtle

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle1.pensize(3)
turtle2.pensize(3)
turtle3.pensize(3)

scr = turtle.Screen()
scr.bgcolor("lightgreen")



#Write a function fizz_buzz(n) that prints the numbers from 1 to n, one per line. For multiples of 3 print Fizz instead of the number, for multiples of 5 print Buzz, and for multiples of both print FizzBuzz. A call to fizz_buzz(16) would produce the following outpu

def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(17)

#Write a function digit_sum(n) that returns the sum of the digits of a non-negative whole number n, using only arithmetic (the % and // operators) and no strings. For example, digit_sum(1234) returns 10, because 1 + 2 + 3 + 4 = 10, and digit_sum(0) returns 0.

def digit_sum(n):
    if n >= 0:
        text = str(n)
        sum = 0
        for i in text:
            sum += int(i)
        return sum
    else:
        print("Please enter a positive integer")

print(digit_sum(1783))

#Write a function alternate_case(s) that returns a new string in which the characters at even positions (0, 2, 4, ...) are upper case and the characters at odd positions (1, 3, 5, ...) are lower case. Spaces and punctuation take up a position too. For example, alternate_case("hello world") returns 'HeLlO WoRlD

def alternate_case(text):
    index = 0
    sum = ""
    for char in text:
        if index % 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        sum += char
        index += 1
    return sum

print(alternate_case("patates kızartması"))

#Write a function draw_polygon(t, sides, length) that makes the turtle t draw a regular polygon with the given number of sides. Then use it, inside a loop, to reproduce the picture below: a red triangle, a yellow square and a blue pentagon, each with side length 60 and drawn with pen size 3. The bottom-left corners of the three shapes are at (-150, -30), (-30, -30) and (90, -30). The turtle starts at (0, 0), facing east.

turtle1.color("red")
turtle2.color("yellow")
turtle3.color("blue")

def draw_polygon(turtle, sides, lenght, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(sides):
        turtle.forward(lenght)
        turtle.left(360/sides)

#draw_polygon(turtle1, 3, 60,0,0)
#draw_polygon(turtle2, 4, 60,100,0)
#draw_polygon(turtle3, 5, 60,200,0)


#Write a function filled_square(t, size, color) that draws a filled square with the given side length and fill colour, starting from the turtle's current position. Use it in a loop to reproduce the picture below: five squares of side 50 in a row, with a gap of 20 between neighbouring squares. The bottom-left corner of the first square is at (-165, -25). The colours alternate: red, blue, red, blue, red

trtsquare = turtle.Turtle()
trtsquare.color("black")
def filled_square(t,size,color):
    trtsquare.fillcolor(color)
    trtsquare.begin_fill()
    for i in range(4):
        trtsquare.forward(size)
        trtsquare.left(90)
    trtsquare.end_fill()

def draw_filled_square1():
    for i in range(5):
        if i % 2 == 0:
            color = "red"
        else:
            color = "blue"
        trtsquare.penup()
        trtsquare.goto(i*70,0)
        trtsquare.pendown()
        filled_square(trtsquare,50,color)

#draw_filled_square1()

#The picture below shows twelve squares of side 80. All of them share one corner at the centre of the window, (0, 0), and each square is turned a little more than the one before. Write a function draw_square(t, size) and use it in a loop to reproduce the picture. Use pen size 2. The turtle starts at (0, 0), facing eas
turtle5 = turtle.Turtle()
def drawsquare(size):
    for i in range(16):

        for i in range(4):
            turtle5.forward(size)
            turtle5.left(90)
        turtle5.right(360/16)

#drawsquare(80)

#Draw a 6 by 6 checkerboard of squares with side length 40, as in the picture below. The bottom-left corner of the board is at (-120, -120). The square in the bottom-left corner is filled black, and the colours alternate along every row and every column. Every square has a black outline. Write a function that draws one square and takes a parameter telling it whether to fill the square, and use nested loops to draw the board
turtle6 = turtle.Turtle()
#turtle.tracer(0)
def draw_filled_square2(x,y,size,color):
    turtle6.penup()
    turtle6.goto(x,y)
    turtle6.pendown()
    turtle6.fillcolor(color)
    turtle6.begin_fill()
    for i in range(4):
        turtle6.forward(size)
        turtle6.left(90)
    turtle6.end_fill()

def draw_checkerboard(lenght):
    color = True

    for i in range(lenght):
        for j in range(lenght):
            if color == True:
                draw_filled_square2(i*40,j*40,40,"lightgreen")
                color = False
            else:
                draw_filled_square2(i*40,j*40,40,"black")
                color = True
        if color == True:
            color = False
        else:
            color = True

draw_checkerboard(6)


#Dostum yemin ederim Artificial Intelligence değil yemin ederim!

scr.exitonclick()