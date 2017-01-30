#!/usr/bin/env python3
import random
answers = ["Salsa", "Salsa!", "SALSA","DID SOME BODY SAY SALSA?!"]
print("Welcome to the Ball of Salsa!")
if 'salsa' in input("What is your question? >>>").lower():
    print("███████╗ █████╗ ██╗     ███████╗ █████╗ ██╗")
    print("██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗██║")
    print("███████╗███████║██║     ███████╗███████║██║")
    print("╚════██║██╔══██║██║     ╚════██║██╔══██║╚═╝")
    print("███████║██║  ██║███████╗███████║██║  ██║██╗")
    print("╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝")
else:
    print=random.choice(answers)
