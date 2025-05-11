import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock , paper , scissors]
user_choice = int(input("what do you want to choose 0 for rock , 1 for paper , 2 for scissors "))
if user_choice >= 0 or user_choice<= 2:
  print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer choose:")
print(game_images[computer_choice])
print(computer_choice)
if user_choice < 0 or user_choice > 2:
    print("you entered invalid input you loose")
elif user_choice == computer_choice:
    print("draw")
elif user_choice > computer_choice:
    print("you win")
elif user_choice == 0 and computer_choice == 1:
    print("sorry you loose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice == 1 and computer_choice == 2:
    print("sorry you loose")




