import random
# Generate a random number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0

print("===================================")
print(" Welcome to Number Guessing Game ")
print(" Guess a number between 1 and 100 ")
print("===================================")

while True:
    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess < secret_number:
        print("Too Low! Try Again.\n")

    elif guess > secret_number:
        print("Too High! Try Again.\n")

    else:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break