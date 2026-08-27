import random

print("Welcome to Guess the number game")
print("I am guessing a number between 1 and 100")

num=random.randint(1,100)

user_guess=int(input("Guess the number: "))



if num==user_guess:
    print("Yoo guessed it right ")
elif num>user_guess:
    print("too low")
elif num<user_guess:
    print("too high")
