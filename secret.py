### Gues the number ###

secret = 99
guess = input("Guess the number")

print(guess)
if int(guess) == int(secret):
    print("You guessed the right number")
else:
    print("Sorry but wrong number")
