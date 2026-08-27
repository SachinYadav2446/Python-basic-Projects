import random

print("Welcome to Guess the number game")
print("I am guessing a number between 1 and 100")

num=random.randint(1,100)

attempts=0
while True:
    user_guess=int(input("Guess the number: "))
    attempts+=1
    if num==user_guess:
        print(f"Guessed it right in {attempts} attempts")
        break
    elif num>user_guess:
        print("too low")
    elif num<user_guess:
        print("too high")

    