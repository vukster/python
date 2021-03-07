import json
from class_def import *
from oop_functions import *


print("What are the names of the players?")
first_name=input("Type in Players First Name")
last_name=input("Type in Players Last Name")
points=input("Type in Players points")
height=input("Type in Players height")
weight=input("Type in Players weight")
rebounds=input("Type in Players rebounds")
assists=input("Type in Players assists")

new_player=BasketballPlayer(first_name=first_name, last_name=last_name, points=points, height=height, weight=weight, rebounds=rebounds, assists=assists)

read_players_json()

all_new_players=new_player.__dict__
players_all.append(all_new_players)

write_players_json()










