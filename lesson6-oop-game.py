import random
import json
import datetime

class result():
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

secret = random.randint(1, 10)
attempts = 0
date = datetime.datetime.now()
print(date)
player_name = str(input("What is your name, please?"))

with open("game-array-results.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

    for score_dict in score_list:
        print("Name: " + str(score_dict["name"] + " had " + str(score_dict["attempts"]) + " attempts, date: " + str(score_dict["date"])))
        print("name")

while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1

    if guess == secret:

        all_results = result(player_name=player_name,attempts=attempts,date=date)
        all_new_results = all_results.__dict__
        score_list.append(all_new_results)

        with open("game-array-results.txt", "w") as player_write:
            player_write.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")