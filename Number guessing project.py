import random
def game(chances):
    print("welcome to the number guessing game")
    computer_guess = random.randint(1,100)
    user_guess = int()
    while chances > 0:
        try:
            user_guess = int(input("guess a number between 1 and 100 "))
        except ValueError:
            print("please enter the valid input")

        if user_guess == computer_guess:
            print("you guessed it right")
            quit()
        elif user_guess > computer_guess:
            print("Too high")
        else:
            print("Too low")

        chances -= 1
        print(f"you have {chances} chances left.\n")

    print(f"you run out of guesses. The computer guess was {computer_guess}")

user_level_input = input("choose the difficulty level 'HARD' or 'EASY' ")
if user_level_input == 'HARD'.lower():
    game(5)
elif user_level_input == 'EASY'.lower():
    game(10)
else:
    print("please enter valid input")



