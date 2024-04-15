print("?????????????")
print()
print("PYTHON SIMPLE QUIZ GAME")
print()
print("?????????????")

questions = [ 
{"Question": "Which is not a Python datatype?", "Answer":"B"},
{"Question": "Using the Set type in Python you can ...", "Answer":"C"},
{"Question": "What can you do with Jupyter notebook?", "Answer":"C"},
{"Question": "What is the meaning of PEP8?", "Answer":"A"},
{"Question": "What is a decorator in Python?", "Answer":"D"}
]

options = [["A. Float", "B. Char", "C."]
           

]

def check_answer(user_guess,correct_answer):
    if user_guess == correct_answer:
        print("Correct!")
    else:
        print("Wrong :( ")

for question in range(len(questions)):
 print("????????????")
 print(questions[question]["Question"])
 for i in options :
     print(i)

guess = input("Enter the answer (A,B,C or D)").upper()
is_correct = check_answer(guess,[questions]["Answer"])