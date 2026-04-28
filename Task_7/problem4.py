
class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.list = []
    def add_player(self, player_obj):
        self.list.append(player_obj)
        print(self.list)                   #check

a = player("mosalah", "11")
b = player("momagdy", "9")
c = player("LionelAndresMessi", "10")

dream_team = Team()
dream_team.add_player(a.name)
dream_team.add_player(b.name)
dream_team.add_player(c.name)