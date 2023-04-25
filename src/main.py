import random

from src.game import Game


def main():
    game = Game()
    game.play()
    game.scoreboard.print_scoreboard()


if __name__ == "__main__":
    main()
