# Program to check Cho/Han - dice roll by A00279670

from random import randint

guess = input("Plese enter your guess (even or odd) : ").lower()

if guess == "even" or guess == "odd" :
    
    dice_roll_1 = randint(1,6)
    dice_roll_2 = randint(1,6)
    total = dice_roll_1 + dice_roll_2
    
    if total % 2 == 0 and guess == "even":
        print(f"Dice roll 1 : {dice_roll_1} \nDice roll 2 : {dice_roll_2} \nTotal : {total} \nYour guessed correctly")
    elif total % 2 == 0 and guess == "odd":
        print(f"Dice roll 1 : {dice_roll_1} \nDice roll 2 : {dice_roll_2} \nTotal : {total} \nYour guessed incorrectly")
    elif total % 2 != 0 and guess == "even":
        print(f"Dice roll 1 : {dice_roll_1} \nDice roll 2 : {dice_roll_2} \nTotal : {total} \nYour guessed incorrectly")
    else:
        print(f"Dice roll 1 : {dice_roll_1} \nDice roll 2 : {dice_roll_2} \nTotal : {total} \nYour guessed correctly")
        
else:
    print("Invalid input")