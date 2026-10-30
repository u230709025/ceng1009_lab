# def sumTo(n):
#     return n * (n + 1) / 2
#
# print(sumTo(10))
#
# n = int(input("Please enter a number : "))
# print("Sum is", sumTo(n))
#
# print(sumTo(10))
# 
# import turtle
#
# def drawStar(t, n , size):
#     angle = 180 - 180 / n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 10, 200)
# wn.exitonclick()
#
# def sumTo(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#     return total
#
# print(sumTo(10))
# n = int(input("Please enter a number: "))
# print("Sum is: ", sumTo(n))
#
# import math
#
# def mySqrt(x):
#    guess = x / 2
#    for i in range(20):
#        guess = (1/2) * (guess + x / guess)
#
#    return guess
#
# n = int(input("Enter a positive integer: "))
#
# print("The result is", mySqrt(n))
# print("The result is", math.sqrt(n))
#
# import turtle
#
#  def drawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
# def drawTip(t, size):
#    t.end_fill()
#    t.left(90)
#    t.forward(size / 2)
#    t.right(90)
#
# def drawSpirateWithTips(someturtle ,legs,lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         drawTip(someturtle, 10)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#    
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("pink")
# t.speed(1)
# t.pensize(2)
#
# def fancySquare (t, size):
#     for corner in range (4):
#         drawSpirateWithTips(t ,8, 20)
#         t.forward(size)
#         t.left(90)
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
# t=turtle.Turtle()
# t.pensize(2)
# fancySquare(t, 100)
# wn.exitonclick()
# 
# wn.exitonclick
#
# def checkSign(x):
#     if x > 0:
#          return "positive"
#     elif x < 0:
#         return "negative"
#     else:
#         return "zero"
#
# numbers = [-7, 5, 0]
#
# for number in numbers:
#     print(number, "is", checkSign(number))
#
# n = int(input("Please enter a number: "))
# print(checkSign(n))
#
#import turtle
#
# def drawBar(t,height ,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(""+ str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
#def barChart(data):
#    maxheight = max(data)
#    num_bars = len(data)
#    border = 10
#
#    gap =(maxheight - border)/ 25
#
#    wn = turtle.Screen()
#    wn.bgcolor("lightgreen")
#
#    right  = 40 * num_bars + border
#    top =maxheight + 4 * gap
#    wn.setworldcoordinates(-border, -border,right,top)
#    t=turtle.Turtle()
#    t.color("blue")
#    t.fillcolor("red")
#    t.pensize(3)
#    for height in data:
#        drawBar(t, height, gap)
#    wn.exitonclick()
#data = [48,117,200,240,160,260,220]
#
#barChart(data)