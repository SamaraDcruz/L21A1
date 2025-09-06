import random

print("Welcome to the number game!")
# Generate a random number between 1 to 10
random_number = random.randint(1, 10)

# Take input from the user
user_guess = int(input("Guess a number between 1 to 10:"))

# Check if the guess is correct
if user_guess == random_number:
    print("🎉 Congratulations! You guessedd it right! 🎉")
else:
    print("❌ Oops! Wrong guess! ❌")
    print("The correct number was", random_number)
