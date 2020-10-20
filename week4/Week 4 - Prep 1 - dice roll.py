# -*- coding: utf-8 -*-
"""
Write a Python program to play the game. The program should allow the player to roll the die up to
4 times, display the roll, and check if the player has rolled a six. If the player has rolled a 6, the
game is over and the player has won. If the player rolls 4 times and hasn't rolled a 6, s/he loses.

@author: kevmc
"""

from random import randint

roll_count = 0
was_six_rolled = False

while roll_count < 4 and was_six_rolled == False:
    print(f"Dice roll number : {roll_count + 1} ")
    roll_count = roll_count + 1
    result = randint(1, 6)
    print(f"{result} was rolled \n")
    
    if result == 6:
        was_six_rolled = True
        

if was_six_rolled == False:
    print(f"Dice was rolled {roll_count} times \n6 not rolled, \nYou lost the game")
else:
    print(f"Dice was rolled {roll_count} times \n6 was rolled, \nYou won the game")