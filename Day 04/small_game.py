#declare a secret number
#guess the number through an input (only get 3 chances)
#optional - declare the guessed number is too low or too high

print("""Guess the secret number between 1 and 10 and win a prize🎁.
Be careful!!! YOU ONLY HAVE 3 CHANCES.""")


secret_number = 5
attempt = 0
max_attempt = 3

while attempt < max_attempt:
    attempt = int(input("Guess the secret number: "))

    if attempt == secret_number:
        print("CONGRATULATIONS!!! You have won a prize🎁")
        exit()
    elif attempt > secret_number:
        print("Your guess is too high.")
    else:
        print("Your number is too low")

    attempt += 1