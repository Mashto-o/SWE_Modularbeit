from src.player import Player


class PlayerTest:

    def perform_tests(self):
        player = Player("John", 3)
        assert str(player) == "John: 3"
        player.update_score(2)
        assert player.score == 2
        player.update_score(4)
        assert player.score == 2
