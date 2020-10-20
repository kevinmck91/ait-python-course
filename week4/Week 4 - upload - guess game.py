# Program to simulate a guessing game with random number generator by A00279670

from random import randint

number = randint(1,100)
guess = -1


for i in range (0,10):
    
    guess = int(input(f"guess the number (guess number {i+1}) : \n"))

    if(guess == number):
        print("correct, You win")
        break;
    elif(guess < number):
        print("guess is too low")
    elif(guess > number):
        print("guess is too high")
    
    guess = -1

if guess == -1:
    print("fail")



