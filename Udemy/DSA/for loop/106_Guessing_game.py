import random

randNum = random.randrange(1, 100)
guess = 0
chance = 7
print("I have guessed a number between 1 to 100.")
print(f"You have {chance} chances to guess the number.")

for i in range(chance):
    guess = int(input("Take a guess: "))
    print(f"Chances remaining: {chance - (i+1)}")
    if guess == randNum:
        print(f"You Guessed it correct!! in {i+1} attempts.")
        break
    elif guess > randNum:
        print("Try smaller number")
    else:
        print("Try bigger number")
print("***** You ran out of chances *****")

# while guess != randNum:
#     guess = int(input("Guess the number from 1 to 10.."))
#     if guess == randNum:
#         print("Congrats!! You got it.")
#     elif guess > randNum:
#         print("Try smaller")
#     elif guess < randNum:
#         print("Try bigger")