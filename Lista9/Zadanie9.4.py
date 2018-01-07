from turtle import *
import math
import random

tracer(0,1)

def kwadrat(a):
    fillcolor('red')
    begin_fill()
    for j in range(4):
        fd(a)
        lt(90)
    end_fill()

def dywan(d,a):
    if d == 0:
        kwadrat(a)
    else:
        for i in range(4):    #reukrencja 
            dywan(d-1,a/3)    #rysuję po dwa mniejsze kwadraty na bok
            fd(a/3)           # jest 8 wiec dobrze sie dzieli
            dywan(d-1,a/3)    #kazdy mniejszy kwadrat to kolejny dywan
            fd(a/3)           #d - glebokosc (ile hcemy dywanow)
            fd(a/3)           #a - bok najwiekszego 
            lt(90)            #a dzielimy na 3 bo na jeden bok
                              #przypadaja 3 mniejsze

dywan(4,400)

input()
