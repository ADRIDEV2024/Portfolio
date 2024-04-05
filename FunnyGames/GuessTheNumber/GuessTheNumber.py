import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def level_dificulty(level_chosen:str):
    
    if level_chosen == "easy":
        attempts = 10
        return EASY_LEVEL_ATTEMPTS 
    else:
        attempts = 5
        return HARD_LEVEL_ATTEMPTS 
    
def check_answer(guess_number,answer:int,attempts:int):
    if guess_number<answer:
        print("Wrong!,the number you are looking for is greater")
        return attempts-1
    elif guess_number>answer:
        print("Wrong!,the number you are looking for is lower")
        return attempts-1
        

print("I have a number between 1 to 100 in my mind")
answer = random.randint(1,100)

print(answer)

level = input("Chosse level dificulty...type <<easy>> or <<hard>>: ")
attempts = level_dificulty(level)
print(f"You have {attempts}remaining to guess my number.")
guess_number = input(int("Guess a number: "))

