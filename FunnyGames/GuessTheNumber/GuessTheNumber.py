import random

EASY_LEVEL_ATTEMPTS = 5
HARD_LEVEL_ATTEMPTS = 3


def level_dificulty(level_chosen:str):
    
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS 
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS 
    else:
        return
    
def check_answer(guess_number,answer:int,attempts:int):
    
    if guess_number<answer:
        print("Wrong!,the number you are looking for is greater")
        return attempts-1
    elif guess_number>answer:
        print("Wrong!,the number you are looking for is lower")
        return attempts-1
        
def play():
    
        print("I have a number between 1 to 100 in my mind")
        answer = random.randint(1,100)

        print(answer)

        level = input("Chosse level dificulty...type <<easy>> or <<hard>>: ")
        attempts = level_dificulty(level)
        
        while guess_number != answer:

            print(f"You have {attempts}remaining to guess my number.")
            guess_number = input(int("Guess a number: "))
            answer= check_answer(guess_number,answer,attempts)

            if attempts == 0:
                print("Sorry,your time to guess has finish. You lose :( ")

            elif guess_number != answer:
                print("Guess again")
                
if __name__ == "__main__":
play()
