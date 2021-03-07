class Player():
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def weight_to_lbs(self):
        pounds = self.weight * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight)
        self.points = points
        self.rebonds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


divac = BasketballPlayer(first_name="Vlade", last_name="Divac", points=28.5, height=2.16, weight=125, rebounds=4.5, assists=5)
jordan = BasketballPlayer(first_name="Michael", last_name="Jordan", points=28.5, height=2.08, weight=105, rebounds=8.5, assists=9.5)
lebron = BasketballPlayer(first_name="Lebron", last_name="James", points=26.5, height=2.10, weight=115, rebounds=9.5, assists=5.5)
ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height=184, weight=79, goals=586, yellow_cards=95, red_cards=11)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height=170, weight=67, goals=575, yellow_cards=67, red_cards=0)