import random

if __name__ == "__main__":
    print("Welcome to the Dice Game!")
    print("Roll the dice and try to guess the number.")

    target_number = random.randint(1, 6)

    while True:
        guess = int(input("Enter your guess (1-6): "))

        if guess < 1 or guess > 6:
            print("Invalid guess. Please enter a number between 1 and 6.")
            continue

        if guess == target_number:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Oops! Wrong guess. Try again.")
