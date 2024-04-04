import random

def play():
 player1 =input(
     "Choose an option: stone, paper or scissors.\n").lower()
 
 computer= print(random.choice(["stone","paper","scissors"]))
 
 if player1 == computer :
      return "¡Tie!"
  
 if win_player(player1,computer):
       return "You win!"
   
 return "You lose"