from src.guess import Guess
from src.player import Player
from src.scoreboard import Scoreboard
from src.wordlist import WordList


class Game:
    def __init__(self):
        self.word_list = WordList("../wordles.txt")
        self.scoreboard = Scoreboard("../scoreboard.txt")
        self.guess = None

    def play(self):
        while True:
            word = self.word_list.get_next_word()
            # print(word)
            if not word:
                print("No more words available!")
                break
            self.guess = Guess(word)

            result = self.guess.run(self.word_list)
            if result:
                print("You won!")
                self.add_score()
            else:
                print("You lost!")

    def add_score(self):
        if input("Do you want to add your score to the scoreboard? (y/n)").lower() == 'y':
            name = input("Enter your name: ")
            player = Player(name, self.guess.get_num_attempts())
            self.scoreboard.add_player(player)