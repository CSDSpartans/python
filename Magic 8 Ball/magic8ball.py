import random
answers = ["Yes", "No", "Maybe","Ask your mother."]

#MAGIC 8 BALL

def game():
    print("Welcome to the Magic 8 Ball!")
    input("What is your question? >>>")
    answer=random.choice(answers)
    print(answer)
    #print(answers[3])

try:
    while True:
        game()
    
except(KeyboardInterrupt):
    print("Thanks for playing!")
    exit

