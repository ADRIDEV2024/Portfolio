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

print("I have a number between 1 to 100 in my mind")
answer = random.randint(1,100)

print(answer)
level = input("Chosse level dificulty...type <<easy>> or <<hard>>: ")

