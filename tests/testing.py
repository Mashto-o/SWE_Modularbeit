import random

from tests.PlayerTest import PlayerTest
from tests.ScoreboardTest import ScoreboardTest
from tests.WordListTest import WordListTest
from tests.WordTest import WordTest


class Testing:
    def __init__(self):
        self.wordTest = WordTest()
        self.wordListTest = WordListTest()
        self.playerTest = PlayerTest()
        self.scoreboardTest = ScoreboardTest()
        self.perform_tests()

    def perform_tests(self):
        self.wordTest.perform_tests()
        self.wordListTest.perform_tests()
        self.playerTest.perform_tests()
        self.scoreboardTest.perform_tests()

if __name__ == "__main__":
    random.seed(42)  # Set seed for reproducibility

    tests = Testing()
    tests.perform_tests()

    print("All tests passed!")
