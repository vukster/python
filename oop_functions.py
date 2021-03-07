import json

def read_players_json():
    with open("all_players.json", "r") as players_read:
        players_all = json.loads(players_read.read())
        return players_all

def write_players_json():
    with open("all_players.json", "w") as players_write:
        player_written.write(json.dumps(players_write))
        print("Wurde eingetragen")
        return()

 ##### Easy Method #####
def write_players_easy():
    with open("football_players.txt", "w") as football_file:
        football_file.write(str(new_player.__dict__))
        print("Wurde eingetragen")
        return()

def append_players():
    players_all.append(new_player.__dict__)
    return