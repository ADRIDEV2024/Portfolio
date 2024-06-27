import QuestionsAnswers as QA


print("\t****** PYTHON SIMPLE QUIZ GAME ******\n")

def check_answer(user_guess:str,correct_answer:str):
    if user_guess == correct_answer:
        print("Correct!")
    else:
        print("Wrong :( ")

for question in range(len(QA.questions)):
 print("*************************")
 print(QA.questions[question]["Question"])
 for i in QA.options[QA.questions] :
     print(i)
     
score = 0
guess = input("Enter the answer (A,B,C or D): ").upper()
is_correct = check_answer(guess,[QA.questions],["Answer"])
if is_correct:
    print("Correct!")
    score+=1
else :
    print("Upps,maybe is Wrong")
    print(f"The correct answer is {QA.questions[question]["Answer"]}")
    score-=1
print(f"Your current score is {score}/{question+1}")    

print(f"Your have given {score} correct answers")
print(f"Your score is {(score/len(QA.questions))*100}%")
