from src.player import Player


class Scoreboard:
    def __init__(self, filename):
        self.filename = filename
        self.players = []
        self.load_scoreboard()

    def load_scoreboard(self):
        with open(self.filename, 'r') as f:
            for line in f:
                name, score = line.strip().split(',')
                self.players.append(Player(name, int(score)))

    def add_player(self, player):
        self.players.append(player)
        self.players.sort(key=lambda x: x.score)
        self.save_scoreboard()

    def save_scoreboard(self):
        with open(self.filename, 'w') as f:
            for player in self.players:
                f.write(f"{player.name},{player.score}\n")

    def print_scoreboard(self):
        for player in self.players:
            print(player)