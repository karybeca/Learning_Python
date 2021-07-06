#!/bin/python3
from turtle import *

speed (0)

penup()
goto(-140,140)

for step in range(15):
  write (step, align='center')
  right (90)
  for bar in range(8):
    forward (10)
    pendown()
    forward(10)
    penup()
  backward(160)
  left (90)
  forward (20)
 # print (step)
  
  
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()
  
bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()

alex = Turtle()
alex.color('green')
alex.shape('turtle')
alex.penup()
alex.goto(-160, 40)
alex.pendown()

sasi = Turtle()
sasi.color('pink')
sasi.shape('turtle')
sasi.penup()
sasi.goto(-160, 10)
sasi.pendown()

from turtle import *
from random import randint

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  alex.forward(randint(1,5))
  sasi.forward(randint(1,5))
  
    