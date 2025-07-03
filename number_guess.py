import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess < 1 or guess > 10:
    print("Invalid guess! Please choose a number between 1 and 10.")
elif guess == secret:
    print("🎉 You got it!")
elif guess != secret:
    print("No! The number was", secret)
