import random


def get_choices():
  options = ["Rock", "Paper", "Scissors"]
  player_choice = input("Enter a choice (Rock, Paper, Scissors: )")
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):

  print(f"You chose {player}, computer chose {computer}")

  if player == computer: 
    return "It's a tie!"

  elif player == "rock": 
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper crumples over rock! You lose."

  elif player == "paper":
    if computer == "rock":
      return "Paper crumples rock! You win!"
    else:
        return "Scissors cuts paper. You Lose"

  elif player == "scissors":
    if computer == "rock":
      return "Rock smashes scissors. You Lose"
    else:
      return "Scissors cuts paper! You win!"
  else:
    return "Select a valid choice"
  
  

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
