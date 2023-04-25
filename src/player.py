class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

    def update_score(self, new_score):
        if new_score < self.score:
            self.score = new_score



