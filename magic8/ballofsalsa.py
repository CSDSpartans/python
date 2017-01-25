#!/usr/bin/env python3
import random
answers = ["Salsa", "Salsa!", "SALSA","DID SOME BODY SAY SALSA?!"]
def game():
    print("Welcome to the Ball of Salsa!")
    if 'salsa' in input("What is your question? >>>").lower():
        print('''███████╗ █████╗ ██╗     ███████╗ █████╗ ██╗
██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗██║
███████╗███████║██║     ███████╗███████║██║
╚════██║██╔══██║██║     ╚════██║██╔══██║╚═╝
███████║██║  ██║███████╗███████║██║  ██║██╗
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝''')
    else:
        print=random.choice(answers)

try:
    while True:
        game()
    
except(KeyboardInterrupt):
    print("Thanks for playing!")
    exit

