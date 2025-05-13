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
choices=[rock,paper,scissors]
user_input=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

if user_input.isdigit() and int(user_input) in [0,1,2]:
    player1 = int(user_input)
    player2 = random.randint(0, 2)

    print("Player 1 choose:")
    print(choices[player1])
    print("Player 2 choose:")
    print(choices[player2])

    if player1 == player2:
        print("it's a draw")
    elif (player1 == 0 and player2 == 2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1):
        print("Player 1 wins")
    else:
        print("Player 2 wins")


else:
    print("You typed the wrong input")




