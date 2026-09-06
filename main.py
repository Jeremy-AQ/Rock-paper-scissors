

import random

actions = ["Rock", "Paper", "Scissors"]
while True:
  while True:
    player_choice = input("Rock, Paper, Scissors, shoot!: ")
    player_choice = player_choice.capitalize()
    if player_choice not in actions:
      print("Please pick Rock, Paper or Scissors")

    else:
      break

  ai_decision = random.choice(actions)
  print(f"The ai chose: {ai_decision}")

  if player_choice == ai_decision:
    print("Its a Tie!")
  elif player_choice == "Rock" and ai_decision == "Scissors":
    print("You Win!")
  elif player_choice == "Rock" and ai_decision == "Paper":
    print("You Lose!")
  elif player_choice == "Paper" and ai_decision == "Rock":
    print("You Win!")
  elif player_choice == "Paper" and ai_decision == "Scissors":
    print("You Lose!")
  elif player_choice == "Scissors" and ai_decision == "Paper":
    print("You Win!")
  elif player_choice == "Scissors" and ai_decision == "Rock":
    print("You Lose!")
  while True:
    Player_Decision = input("Would you like to play again?: ").capitalize()
    if Player_Decision in ["Yes", "No"]:
      break
    print("Please choose YES or NO")

  if Player_Decision == "Yes":
    print("Ok! Lets go again")
    continue

  else:
    print("Thanks for playing!")
    break




