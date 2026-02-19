import random

number=random.randint(1,10)

def guess_game(attempts=1):
    guess=int(input("Guess the number (1 to 10):"))

    if guess==number:
        print(f"correct! you guessed it in {attempts}attempts")
        return
    else:
        print("wrong guess, try again!")
        guess_game(attempts+1)

guess_game()
