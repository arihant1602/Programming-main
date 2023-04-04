from random import randint

a = randint(0, 100)
attempts = 1

while True:
    guess = int(input("Enter your guess\n"))

    if guess > a:
        print("Lower!")
    elif guess < a:
        print("Higher!")
    elif guess == a:
        print("Correct!")
        break
    else:
        print("invalid input")
        break
    attempts += 1

print(f"You solved in {attempts} attempts!")