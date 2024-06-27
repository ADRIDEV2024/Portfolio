import random

def play():
 player = input("Choose an option: stone, paper or scissors.\n").lower()
 
 computer = print(random.choice(["stone","paper","scissors"]))
 
 if player == computer :
      return "¡Tie!"
  
 if win_player(player,computer):
       return "You win!"
   
 return "You lose"

def win_player(player,computer):
    # Return True if the player wins  
    # Stone wins scissors(Stone > Scissors).
    # Paper wins Stone(Paper > Stone).
    # Scissors wins paper(Scissors > Paper).
    
    if ((player1 == "stone" and computer == "scissors")  
             or (player1 == "paper" and computer == "stone")
              or (player1 == "scissors" and computer =="paper")) :
          return True
      
    else :
        return False
    

print(play())

