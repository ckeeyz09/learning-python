import random
import sys
import os

print("How many sides is your die?")

die = int(sys.stdin.readline())

def rollDice(num):
    roll = random.randrange(1, num + 1)
    return (roll)

print ("Your D",die,"roll is:",rollDice(die))