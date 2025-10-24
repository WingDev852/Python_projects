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

import random

game_images = [rock, paper, scissors]
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors '))
if player_choice >= 0 and player_choice <= 2:
    print(game_images[player_choice])

computer_choice = random.randint(0, 2)
print('The computer chose:')
print(game_images[computer_choice])


if player_choice >= 3 or player_choice < 0:
    print('you gave the wrong input')
elif player_choice == 0 and computer_choice == 2:
    print('You Win')
elif computer_choice == 0 and player_choice == 2:
    print('You lose')


elif computer_choice > player_choice:
    print("You Lose")

elif player_choice > computer_choice:
    print('Yoy Win')
elif computer_choice == player_choice:
    print('Its a Draw')

