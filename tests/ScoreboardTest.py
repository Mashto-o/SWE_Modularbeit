from src.player import Player
from src.scoreboard import Scoreboard


class ScoreboardTest:
    def perform_tests(self):
        # Create a test file with some player names and scores
        with open("test_scoreboard.txt", "w") as f:
            f.write("John, 3\nJane, 5")

        scoreboard = Scoreboard("test_scoreboard.txt")
        assert len(scoreboard.players) == 2

        player = Player("Sam", 4)
        scoreboard.add_player(player)
        assert len(scoreboard.players) == 3
        scoreboard.save_scoreboard()

        # Clean up the test file
        import os
        os.remove("test_scoreboard.txt")
